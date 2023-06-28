1. vim .env
```bash
AIRFLOW_IMAGE_NAME=<image name>
AIRFLOW_UID=50000
```
2. Build image.
```bash
docker build -t <image name> .
```

3. 
```bash
docker compose up -d
```

4. Set up connections and variables.
 - aws_credentials
 - bucket_name
 - redshift_connection_info
 - postgres_connection_info

