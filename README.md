### install packages
1. pipenv install "fastapi[standard]"
2. pipenv install sqlmodel==0.0.22
3. pipenv install alembic==1.14.0
4. pipenv install asyncpg==0.30.0
5. pipenv install argon2-cffi==23.1.0
6. pipenv install "psycopg[binary,pool]"
7. pipenv install pydantic-settings==2.7.0
8. pipenv install greenlet==3.1.1
9. pipenv install loguru==0.7.3
10. pipenv install redis==5.0.3 celery==5.3.6 flower==2.0.1 redisbeat==1.2.6 jsonpickle==1.4.2
11. pipenv install fastapi-mail==1.4.2 aiosmtplib==3.0.2 email-validator==2.2.0


#### docker commands
- docker network create <nextgen_local_nw>
- docker compose -f <local.yml> config
- docker compose -f <local.yml> up --build -d --remove-orphans
- docker compose -f <local.yml> down -v
- docker compose -f <local.yml> exec postgres psql -U <augusto> -d <nextgen>
