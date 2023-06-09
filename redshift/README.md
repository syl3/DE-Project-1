vim .pgpass

chmod 600 .pgpass

export PGPASSFILE=/Users/szuyuanlee/Documents/Side\ Project/start_data_engineer/b_beginner_de_project_local/redshift/.pgpass

psql -h sde-redshift-cluster.csvk1p0iy8zw.us-east-1.redshift.amazonaws.com -p 5439 -d dev -U sde_user

\i setup.sql