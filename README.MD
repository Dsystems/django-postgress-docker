# Getting started

> Create virtual env:

```bash
python3 -m venv .venv39
```
> Activate: 
```bash
source .venv39/bin/activate.bash

OR for the Fish shell:

source .venv39/bin/activate.fish
```


> Build docker image from project folder:
> 
```bash
docker-compose build
```

> Make database migrations:

```bash
docker-compose run django python manage.py makemigrations

docker-compose run django python manage.py migrate
```
> Create admin user for Django:

```bash
docker-compose run django python manage.py createsuperuser
```

> Init project:

```bash
 docker-compose up
 ```