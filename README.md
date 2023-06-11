# 1. Objective

Let’s assume that you work for a user behavior analytics company that collects user data and creates a user profile. We are tasked with building a data pipeline to populate the user_behavior_metric table. The user_behavior_metric table is an OLAP table, meant to be used by analysts, dashboard software, etc. It is built from

1. user_purchase: OLTP table with user purchase information.
2. movie_review.csv: Data sent every day by an external data vendor.


![Alt text](img/ERD.png?raw=true "ERD")

# 2. Design
We will be using Airflow to orchestrate the following tasks:

1. Classifying movie reviews with Apache Spark.
2. Loading the classified movie reviews into the data warehouse.
3. Extracting user purchase data from an OLTP database and loading it into the data warehouse.
4. Joining the classified movie review data and user purchase data to get user behavior metric data.
![Alt text](img/design.jpg?raw=true "Optional Title")
We will use metabase to visualize our data.

# 3. Setup

1. Download data
```bash
wget https://start-data-engg.s3.amazonaws.com/data.zip && unzip -o data.zip && chmod -R u=rwx,g=rwx,o=rwx data
```

2. 
```bash
python containers/postgres/transform_time.py
```

3. Create folder.
```bash
chmod -R 777 containers/shared/
```

4. Set up AWS infra.
```bash
terraform apply -auto-approve
```

5. Set up redshift. Follow redshift/README.md

6. Set up airflow. Follow containers/airflow/README.md

7. Set up postgres. Follow containers/postgres/README.md

# 4. Result

![Alt text](img/airflow-grid.png?raw=true "Airflow Grid")
![Alt text](img/airflow-graph.png?raw=true "Airflow Graph")
![Alt text](img/metabase.png?raw=true "Metabase")


**Credit:** 

    https://www.startdataengineering.com/post/data-engineering-project-for-beginners-batch-edition/

    https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main


