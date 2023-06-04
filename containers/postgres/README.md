1. 
```bash
docker compose up -d
```
2. 
```bash
yoyo apply -d postgresql://project:qweasdzxc@localhost:5434/postgres ../../migrations
```
3. 
```bash
pgcli postgresql://project:qweasdzxc@localhost:5434/postgres
```
4. 
```
\i create_user_purchase.sql
```