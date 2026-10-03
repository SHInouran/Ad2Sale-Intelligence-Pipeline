import sys

# Dictionary to store aggregated data
campaigns = {}

# 1. Processing the input
for line in sys.stdin:
    line = line.strip()
    if not line or "\t" not in line:
        continue

    try:
        key, value = line.split("\t")
        
        # Skip the header row if it passed through the Mapper
        if key == "Campaign_ID":
            continue
            
        v_parts = value.split("|")
        
        camp_id = key
        impres = float(v_parts[4])
        engage = float(v_parts[5])
        clicks = float(v_parts[6])
        
        if camp_id not in campaigns:
            campaigns[camp_id] = [
                v_parts[0], v_parts[1], v_parts[2], v_parts[3], 
                impres, engage, clicks
            ]
        else:
            campaigns[camp_id][4] += impres
            campaigns[camp_id][5] += engage
            campaigns[camp_id][6] += clicks
            
    except (ValueError, IndexError):
        continue

# 2. Final Output with Header
# Manually define the column names for your final CSV/Table
header = "Campaign_ID,Age_Group,Duration,Product,Channel,Total_Impressions,Total_Engagement,Total_Clicks"
print(header)

for camp_id, data in campaigns.items():
    # Convert numeric data back to string for printing
    output_row = [camp_id] + [str(x) for x in data]
    print(",".join(output_row))