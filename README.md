# api-flask


https://flask.palletsprojects.com/en/stable/installation/#virtual-environments
python3 -m venv env-api
./env-api/bin/activate

--------------------
sin run.py
flask --app  app --debug run

con run.py
python3 run.py
----------------------


en python anywhere

https://help.pythonanywhere.com/pages/Flask/

mkvirtualenv --python=/usr/bin/python3.10 my-virtualenv

gil clone

pip install -r requirements.txt 

which python


----
WSGI (Web Server Gateway Interface) 
import sys

path = '/home/cesar2025/api-flask'
if path not in sys.path:
    sys.path.append(path)

from app import app as application 