# Getting started

You need [Docker](https:/docker.com/) and [docker-compose](https://docs.docker.com/compose/reference/) installed on your system.
<br>
We recommend to perform all actions inside the virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate.bash
OR for fish shell:
source .venv/bin/activate.fish
```


## ⚙️ Developement mode 

> Build docker image from the project folder:

```bash
docker-compose up --build
```
*Test: http://localhost:8000/*

> Example of manage.py command (creates django admin user):

```bash
docker-compose run django python manage.py createsuperuser
```

> Stop & start containers:

```bash
docker-compose stop
docker-compose start
```

***

## 🚀 Production mode
> Edit files "**.env.prod**" and "**app/entrypoint.prod.sh**" and run command for deploying:

```bash
docker-compose -f docker-compose.prod.yml up --build
```

*Test: http://localhost:1337/*

--- 

## File structure:

```
├─ app/
    ├─ core/          <----------------------
    ├─ portfolio/        └ Django application
    Dockerfile
    Dockerfile.prod
    entrypoint.sh
    entrypoint.prod.sh
    requirements.txt  <-- pip packages
    manage.py
├─ database/          <-- database files
    ├─ postgress/
├─ nginx/             <-- Nginx (for production mode)
    ├─ Dockerfile
    ├─ nginx.conf
.env.dev              <----------------------
.env.prod               └ Environment varibles
.docker-compose.yml
.docker-compose.prod.yml
.gitignore
.dockerignore
```


***

## 🚧 Troubleshooting

... to be soon ...