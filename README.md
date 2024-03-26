# End To End News📰 Data Pipeline with Apache Airflow Snowflake & AWS Services


https://github.com/SiddharthUchil/news-data-pipeline-Airflow-Snowflake-AWS/assets/36127139/2b8f1e3b-1d8a-4ff4-a109-9a5c4d74a958

![alt text](https://github.com/SiddharthUchil/news-data-pipeline-Airflow-Snowflake-AWS/blob/main/pipeline.jpg)
## Overview
This project outlines an automated pipeline for gathering the latest news on a specified topic using the News API, transforming the data into an efficient format, and storing it for analysis. The pipeline is orchestrated using Apache Airflow and utilizes AWS services and Snowflake for storage and data warehousing.

## Architecture
The pipeline operates in four main stages:

1. **Extract News Information**: Utilizes a Python function to fetch news data (title, URL, author, etc.) and convert it from JSON to Parquet format.
2. **Move File to S3**: Transfers the Parquet files to an AWS S3 bucket for persistent storage.
3. **Snowflake Create Table**: Creates a new table in Snowflake, inferring the schema from the Parquet file.
4. **Snowflake Copy**: Copies the data from the S3 bucket into the Snowflake table for querying and analysis.

## Components

### Airflow Scheduler
- **DAG**: Defines the sequence of tasks and their dependencies.
- **PythonOperator**: Executes the Python function for data extraction.
- **BashOperator**: Handles the transfer of files to the S3 bucket.
- **SnowflakeOperator: Used to execute SQL commands in our Snowflake database
### AWS Services
- **S3 Bucket**: Stores the news data in Parquet format.
- **IAM**: Manages access permissions to AWS resources.

### Snowflake
- **Tables**: Stores structured news data.
- **Infer Schema**: Automatically detects the schema from Parquet files.
- **Copy Into**: Transfers data from S3 to Snowflake.

## Setup Instructions

### Prerequisites
- Apache Airflow installed and configured.
- AWS account with S3, IAM roles set up.
- Snowflake account with necessary permissions.

### Configuration
1. Define your Airflow DAG with the specified tasks and schedule.
2. Set up the S3 bucket and ensure the correct IAM roles are in place for access.
3. Configure Snowflake to connect to your S3 bucket and set up automatic schema inference.

## Usage
Once the pipeline is configured, it will run according to the schedule defined in the Airflow DAG. The news data will be automatically fetched, transformed, and stored for further analysis.

## Conclusion
This pipeline provides a robust and scalable solution for news data aggregation and storage, leveraging the power of cloud services and modern data warehousing techniques.
