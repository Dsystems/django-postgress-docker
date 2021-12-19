# Getting started

> Virtual env:
> 
```bash
python3 -m venv .venv39

source .venv39/bin/activate.bash

or

source .venv39/bin/activate.fish

```


> Build docker image from project folder:
> 
```bash
docker-compose build
```

> Make database migrations:

```bash
docker-compose run web python manage.py makemigrations

docker-compose run web python manage.py migrate
```
> Create admin user for Django:

```bash
docker-compose run web python manage.py createsuperuser
```

> Run the server:

```bash
 docker-compose up
 ```