import logging
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from news_fetcher_etl import runner
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


args = {"owner": "Airflow", "start_date": airflow.utils.dates.days_ago(2)}

dag = DAG(
    dag_id="snowflake_automation_dag", default_args=args, schedule_interval=None
)


snowflake_query = [
"""
    create table if not exists source_table (emp_no int, emp_name text, salary int, hra int, Dept text);
""",
    """INSERT INTO source_table VALUES (100, 'A', 2000, 100, 'HR'),
    (101, 'B', 5000, 300, 'HR'),
    (102, 'C', 6000, 400, 'Sales'),
    (103, 'D', 7000, 500, 'Marketing'),
    (104, 'E', 8000, 600, 'Tech'),
    (105, 'F', 9000, 700, 'Finance'),
    (106, 'G', 10000, 800, 'Compliance');
    """
]

with dag:
    
    create_table=SnowflakeOperator(
        task_id="create_table",
        sql=snowflake_query[0],
        snowflake_conn_id="snowflake_conn"
    )
    
    
    insert_data=SnowflakeOperator(
        task_id="insert_snowflake_data",
        sql=snowflake_query[1],
        snowflake_conn_id="snowflake_conn"
    )
    

create_table >> insert_data