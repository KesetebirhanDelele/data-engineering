# Setting up Virtual Environment

pip install virtualenv 

# Installing Python in Virtual Environment

python -m venv venv

(if doesn't work, Run pip uninstall virtualenv and then pip install virtualenv)

Then close and open the terminal to activate the virtual environment by clickin new terminal and then selecting command prompt

# Activating python stored within virtual environment
# (https://www.youtube.com/watch?v=LZUCVqMDgP8&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=5)
Select view, go to command palette and search for python select interpreter
then type .\venv\Scripts\python.exe

# Activate Virtual Environment: type the following in command prompt
venv\Scripts\activae.bat 

# Install FastAPI files in virtual environment
pip install fastapi[all]

# Install underlying driver to allow python talk to sql database
pip install psycopg2

# Install sqlalckemy
pip install sqlalchemy

# Troupblshouting pydantic ORM error 
site-packages/pydantic/_internal/_config.py:261 UserWarning: Valid config keys have changed in V2:* 'orm_mode' has been renamed to 'from_attributes'

Apparently it installed pydantic 2.0.2.

pip install pydantic==1.10.0

# Reading a path environment in Windows using Command Prompt
C:\Users\keset>echo %Path%      
> Note that in Windows, you need to close and restart Command Prompt to read a path variable that has been added 

# Reading a path environment in Windows using Python

import os

path = os.getenv("my_db_url")

print(path)

# Setting environment variables in MAC for Postgresql using Terminal (No GUI as in Windows)
export my_db_url = *localhost:5432*     
# Reading environment variables in Ubuntu
printenv
OR
% echo %my_db_url

# .gitignore file should have environment setting given values file which should never be uploaded to git
.env

# Alembic reference
https://alembic.sqlalchemy.org/en/latest/index.html

# Install alembic to track changes in database and rollback
> SQLAlchemy can only create a database if it doesn't exist already. It can't make modifications.

pip install alembic

# See alembic commands
alembic --help

# Create alembic directory
alembic init alembic

# See alembic revision options to track changes
alembic revision --help

# Create alembic version for a revision
alembic revision -m "create posts table"

# Create your first table using alembic data migration tool
alembic upgrade c6d2d505f0ff

# See the latest revision
alembic heads

# modify a table using all latest revisions
alembic upgrade head

# modify a table with revsion one level higher than the current one
alembic upgrade +1

# Go back to the previous database version
alembic downgrade -1

# Check revision version
alembic current 

# See all history of revisions
alembic history

# How to auto-generate tables in postgres by looking at difference from sqlalchemy models
alembic revision --autigenerate -m "auto-vote"

# how to make api request from Google Chrome but with CORS error
fetch('http://localhost:8000/').then(res => res.json()).then(console.log)

# middleware is a term that's used in most web frameworks because it's basically a function that runs before every request so if someone sends a request to our app and before it actually goes through routers it'll actually go through the middleware and then our middleware can perform some sort of operation

# Documenting requirements
pip freeze > requirements.txt

# Installing all requirements at once
pip install -r requierements.txt

# Setting up git repository for fast api
git init
git add --all
git commit -m "initial commit"
git config --global user.email kesetebirhan@gmail.com
git config --global user.name Kesetebirhan Delele
git branch -M main
git remote add origin https://github.com/KesetebirhanDelele/fastapi.git
git push -u origin main

# Getting Started on Heroku with Python
Install the Heroku Command Line Interface (CLI); You can use the CLI to manage and scale your applications, provision add-ons, view your logs, and run your application locally.

# Verify Heroku installation by looking at version installed
heroku --version

# login into heroku
heroku login

heroku create fastapi-kesete

git push heroku main

# See remote branches set-up
git remote

# create an app in Heroku
git push heroku main

# Creating Docker image to run application using Optimization
FROM python:3.9.7

WORKDIR /usr/src/app

# Copying requirements in current directory which is /usr/src/app
COPY requirements.txt ./

# Installing requiremnts
RUN pip install --no-cache-dir -r requirements.txt

# Copy source codes into current directory.
# Implementation of these codes follows line by line. 
# If nothing changes, COPY command copies last image
# without the need to copy requiremnts and do a pip install
COPY . .

# Finally we have to give it the command that we want to run when 
# we start the container
CMD ["unvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Command to start building image
docker build -t fastapi .

# See list of docker images
docker image ls

docker compose is used to automaticaly spin multiple containers and close them out aswell

