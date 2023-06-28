# 1. Intro

This project originated from [josephmachado](https://github.com/josephmachado/beginner_de_project). Due to the simplicity of the task and the long startup time and high cost of EMR (Elastic MapReduce), I replaced the EMR component with a local Spark Docker container. This allows for faster development and avoids cost pressure during the initial practice and Spark development. Once familiar with the setup, it can be switched back to the original architecture.

# 2. Objective

Let’s assume that you work for a user behavior analytics company that collects user data and creates a user profile. We are tasked with building a data pipeline to populate the user_behavior_metric table. The user_behavior_metric table is an OLAP table, meant to be used by analysts, dashboard software, etc. It is built from

1. user_purchase: OLTP table with user purchase information.
2. movie_review.csv: Data sent every day by an external data vendor.


![Alt text](img/ERD.png?raw=true "ERD")

# 3. Design
We will be using Airflow to orchestrate the following tasks:

1. Classifying movie reviews with Apache Spark.
2. Loading the classified movie reviews into the data warehouse.
3. Extracting user purchase data from an OLTP database and loading it into the data warehouse.
4. Joining the classified movie review data and user purchase data to get user behavior metric data.
![Alt text](img/design.jpg?raw=true "Optional Title")
We will use metabase to visualize our data.

# 4. Setup

## Prerequiements  
1. [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  
2. [Github account](https://github.com)  
3. [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)  
4. [AWS account](https://aws.amazon.com)  
5. [Docker](https://docs.docker.com/engine/install/) with at least 4GB of RAM and [Docker Compose](https://docs.docker.com/compose/install/) v1.27.0 or later  
6. [psql](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  

## Steps

1. Download data.
```bash
wget https://start-data-engg.s3.amazonaws.com/data.zip && unzip -o data.zip && chmod -R u=rwx,g=rwx,o=rwx data
```

2. Transform data time.
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

5. Set up redshift. Follow [README.md](./redshift/README.md)

6. Set up airflow. Follow [README.md](./containers/airflow/README.md)

7. Set up postgres. Follow [README.md](./containers/postgres/README.md)

# 5. Result

![Alt text](img/airflow-grid.png?raw=true "Airflow Grid")
![Alt text](img/airflow-graph.png?raw=true "Airflow Graph")
![Alt text](img/metabase.png?raw=true "Metabase")

# 6. Next Steps
1. CI CD pipeline.
2. Integrations or unit tests.
3. DBT.

**Credit:** 

    https://www.startdataengineering.com/post/data-engineering-project-for-beginners-batch-edition/

    https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main


