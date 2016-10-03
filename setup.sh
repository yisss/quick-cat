#!/bin/bash

python3 -m venv sandbox
. sandbox/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
