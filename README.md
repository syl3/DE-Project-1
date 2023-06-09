1. 
```bash
wget https://start-data-engg.s3.amazonaws.com/data.zip && unzip -o data.zip && chmod -R u=rwx,g=rwx,o=rwx data
```

2. 
```bash
python containers/postgres/transform_time.py
```

3. 
```bash
chmod -R 777 containers/shared/
```

4. 
```bash
terraform apply -auto-approve
```

5. redshift/README.md

6. containers/airflow/README.md

7. containers/postgres/README.md

