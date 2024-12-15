#!/bin/bash

# Virtual Environment set up ~!
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt

# DB setup ~!
python3 ./db/initDb.py #initializes all tables!
python3 ./db/importData.py 