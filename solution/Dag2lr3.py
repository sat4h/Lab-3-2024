# Dag2lr3.py

from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import os

os.environ["AWS_ACCESS_KEY_ID"] = "minio"
os.environ["AWS_SECRET_ACCESS_KEY"] = "minio123"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://minio:9000"

default_args = {
    'owner': 'sat4h',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG(
    'validate_model',
    default_args=default_args,
    description='',
    schedule_interval=None,
)

validate_model = BashOperator(
    task_id="validate_model",
    bash_command="python /opt/airflow/data/validate.py",
    dag=dag
)

validate_model
