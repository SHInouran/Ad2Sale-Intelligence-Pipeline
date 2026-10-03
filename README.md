# 📊 End-to-End Marketing Analytics & Sales BI Pipeline

![Apache Hadoop](https://img.shields.io/badge/Apache%20Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=black)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Microsoft SQL Server](https://img.shields.io/badge/SQL%20Server-CC292B?style=for-the-badge&logo=microsoftsqlserver&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

An end-to-end Big Data & Business Intelligence pipeline that bridges marketing ad performance with e-commerce transactional data. The architecture ingests raw logs into HDFS, applies MapReduce and PySpark MLlib for sentiment analysis and customer clustering, orchestrates ETL flows using SSIS, models a Star Schema Data Warehouse in SSMS, builds an SSAS OLAP Cube with MDX KPIs, and delivers interactive analytics via Power BI Live Connect.

---

## 🛠️ Architecture Overview

```text
 ┌────────────────────────┐
 │   HDFS Raw Data Storage│ (CSV, Social Media Logs)
 └───────────┬────────────┘
             │
 ┌───────────▼────────────┐
 │  Hadoop MapReduce Job  │ (Filtering, Aggregation)
 └───────────┬────────────┘
             │
 ┌───────────▼────────────┐
 │ Apache Spark (PySpark) │ (Sentiment Scoring & K-Means Clustering)
 └───────────┬────────────┘
             │
 ┌───────────▼────────────┐
 │  SSIS ETL Pipeline     │ (Extraction, Cleansing, Transformation)
 └───────────┬────────────┘
             │
 ┌───────────▼────────────┐
 │ SSMS Data Warehouse    │ (Star Schema Data Model)
 └───────────┬────────────┘
             │
 ┌───────────▼────────────┐
 │ SSAS Multidimensional  │ (OLAP Cube & MDX KPIs)
 └───────────┬────────────┘
             │
 ┌───────────▼────────────┐
 │ Power BI Dashboards    │ (Live Connect Dashboards)
 └────────────────────────┘
```

---

## 📁 Repository Structure

```text
.
├── HadoopFile/                
|    ├── Map.py
|    |── Reduce.py
|    |── Saprk.py
|    |── csv files
├── SSIS_pipeline_etl/                   # SSIS ETL control and data flow packages + SQL pipeline
├── SSAS_pipeline/                       # SSAS Multidimensional project files & MDX calculations
|── rapport_final_du_projet.pdf          # french report explaining in details the whole project
└── project_marketing.pbix               # Power BI (.pbix) templates for Live Connect views
```

---

## ⚙️ Key Pipeline Components

### 1. Big Data Processing (Hadoop & MapReduce)
* Ingests raw transactional and social ad data into **HDFS** (`/marketing_project`).
* Executes a **MapReduce job** using Hadoop Streaming (`python3 Map.py` and `python3 Reduce.py`) to aggregate campaign impressions, engagements, and clicks by target segment.

### 2. Data Mining & Customer Segmentation (PySpark MLlib)
* Calculates sentiment scores from customer reviews using a text-mining UDF.
* Features vectorization via `VectorAssembler`.
* Determines the optimal cluster count using the **Elbow Method**.
* Applies **K-Means Clustering** to segment users into distinct behavioral profiles (`persona_cluster`).

### 3. ETL & Data Warehousing (SSIS & SSMS)
* **SSIS:** Orchestrates data pipelines using `Merge Join`, `Derived Column`, and `Multicast` transformations.
* **SSMS Star Schema:** Centers around `fact_marketing_operations` connected to dimensions (`dim_clie`, `dim_produits`, `dim_orders`, `dim_time`, `dim_Camp`, `Dim_Rev`).
* **T-SQL Optimization:** Implements robust SQL views (`v_Fact_Sales`, `v_Fact_Marketing`) using `TRY_CAST` and `ROUND` to handle corrupted numerical types and trailing decimals cleanly.

### 4. SSAS OLAP Cube & MDX KPIs
* **OLAP Engine:** Multidimensional deployment on Analysis Services.
* **MDX Metrics:**
  * **CTR (Click-Through Rate):** `[Clicks] / [Impressions]`
  * **Engagement Rate:** `[Engagements] / [Impressions]`
  * **AOV (Average Order Value):** `[Total Amount] / [Count]`
  * **RPM:** `([Total Amount] / [Impressions]) * 1000`
  * **Conversion Rate:** `[Quantity] / [Clicks]`
* Configured state indicators and gauges for operational performance tracking.

### 5. Interactive Power BI Dashboards
Connected via **Live Connect** for real-time querying without client-side memory load:
1. **Sales Performance Dashboard:** Tracks product revenues, order volumes, and ratings correlation.
2. **Marketing Performance Dashboard:** Evaluates campaign channel efficiency (CTR, Engagement Rate by Age/Platform).
3. **Customer Experience & Persona Dashboard:** Visualizes revenue-per-mille (RPM) and AOV broken down by Spark-generated customer clusters.

---

## 🚦 Getting Started

### Prerequisites
* Hadoop (HDFS & MapReduce / Streaming)
* Apache Spark (PySpark & MLlib)
* Microsoft SQL Server & SSMS
* SQL Server Integration Services (SSIS)
* SQL Server Analysis Services (SSAS Multidimensional)
* Power BI Desktop

### Quick Step-by-Step Execution

1. **Upload Data to HDFS & Run MapReduce:**
   ```bash
   hadoop fs -mkdir -p /marketing_project
   hadoop fs -put ./data/* /marketing_project/
   
   hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
     -files Map.py,Reduce.py \
     -mapper "python3 Map.py" \
     -reducer "python3 Reduce.py" \
     -input /marketing_project/Social_Media_Advertising.csv \
     -output /marketing_project/output_results
   ```

2. **Run PySpark Data Mining Job:**
   ```bash
   spark-submit spark_job.py
   ```

3. **Deploy Database & SSIS:**
   * Run the SQL scripts in `SQL_Scripts/` to create database objects.
   * Open and execute the SSIS package (`SSIS_Pipeline/`) to populate the Star Schema.

4. **Deploy SSAS & Connect Power BI:**
   * Build and process (`Process Full`) the SSAS multidimensional project in Visual Studio.
   * Open Power BI Desktop, choose **Analysis Services (Live Connect)**, and select the deployed cube.

---

## 👩‍💻 Author
**Bouchama Nourane**  
*École Nationale Polytechnique — Industrial Engineering (DSIA)*  
*Academic Year: 2025/2026*
