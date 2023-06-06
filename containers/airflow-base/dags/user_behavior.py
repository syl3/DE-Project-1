from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

# DAG definition
default_args = {
    "owner": "airflow",
    "depends_on_past": True,
    "wait_for_downstream": True,
    "start_date": datetime(2021, 5, 23),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
    #"template_searchpath" : ["/opt/airflow/dags"]
}

dag = DAG(
    "user_behavior",
    default_args=default_args,
    schedule_interval="0 0 * * *",
    max_active_runs=1,
    catchup=False
)

extract_user_purchase_data = PostgresOperator(
    dag=dag,
    task_id="extract_user_purchase_data",
    sql="./scripts/sql/unload_user_purchase.sql",
    postgres_conn_id="postgres_1",
    params={"user_purchase": "/shared/temp/user_purchase.csv"},
    depends_on_past=True,
    wait_for_downstream=True,
)



end_of_data_pipeline = DummyOperator(task_id="end_of_data_pipeline", dag=dag)

extract_user_purchase_data >> end_of_data_pipeline