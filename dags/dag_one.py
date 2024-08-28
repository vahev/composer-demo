from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def print_hello():
    print("Hello from Airflow!")


with DAG(
    'sample_dag',
    description='A simple DAG to test deployment',
    schedule_interval=None,  # Run manually or trigger it
    start_date=datetime.now(),
    catchup=False
) as dag:

    hello_task = PythonOperator(
        task_id='hello_task',
        python_callable=print_hello
    )
