1. Create .pgpass
```bash
echo sde-redshift-cluster.csvk1p0iy8zw.us-east-1.redshift.amazonaws.com:5439:dev:sde_user:sdeP0ssword0987 >> .pgpass
```

2. 
```bash
chmod 600 .pgpass
```

3. 
```bash
export PGPASSFILE=path_to/.pgpass
```
4. 
```bash
psql -h sde-redshift-cluster.csvk1p0iy8zw.us-east-1.redshift.amazonaws.com -p 5439 -d dev -U sde_user
```
5. 
```sql
\i setup.sql
```
