#!/bin/bash

# Virtual Environment set up ~!
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt

# DB setup ~!
mkdir db
touch ./db/app.db