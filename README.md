# Cookie Stand API

Backend API for accessing cookie stand information.

Uses ElephantSQL postgres database

Lab 41: deployed to Vercel

## Author: Mike Shen

## Links and Resources

https://cookie-stand-admin-pi-orpin.vercel.app/

https://cookie-stand-rinqjud97-mikeshen7.vercel.app/api/v1/app/

##  Setup
Create elephantSQL instance

Need to set up root/.env and CookieStand/.env files for Django secret key.  See .env.sample

docker compose up --build

# How to initialize/run your application (where applicable)

1. Build docker container: docker compose up --build
2. With docker running: docker compose run web python manage.py migrate
3. With docker running: docker compose run web python manage.py createsuperuser


Routes:
1. Get a token: http post localhost:8000/api/token/ username=admin password=YOUR_PASSWORD 
2. Refresh token: http post localhost:8000/api/refresh/ refresh=REFRESH_TOKEN_HERE 
3. Roster list: http localhost:8000/api/v1/app/ "Authorization: Bearer ACCESS_TOKEN_HERE"
4. Roster detail: http localhost:8000/api/v1/app/{pk} "Authorization: Bearer ACCESS_TOKEN_HERE"
- where {pk} is the primary key of the player
5. Admin: http://localhost:8000/admin



## How to use your library (where applicable)

## Tests

Modify CookieStand/.env to use local database

Modify docker-compose.yml to use local database

docker compose run web python manage.py test

Manually tested API using HTTPie

Manually tested JWT using HTTPie