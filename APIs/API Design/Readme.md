# Setting up Virtual Environment

pip install virtualenv 

# Installing Python in Virtual Environment

python -m venv venv

(if doesn't work, Run pip uninstall virtualenv and then pip install virtualenv)

# Installing FastAPI

pip install fastapi "uvicorn[standard]"

# Troupblshouting pydantic ORM error
site-packages/pydantic/_internal/_config.py:261 UserWarning: Valid config keys have changed in V2:* 'orm_mode' has been renamed to 'from_attributes'

Apparently it installed pydantic 2.0.2.

pip install pydantic==1.10.0

