# Arc-API
A RESTful API backend service using FASTAPI, designed to Create, Read, Update, and Delete requests for Items.

## What is the purpose of Arc-API?
The purpose of Arc-API is simple: Sending requests to create, read, update, and delete items into a SQLite database.
The SQLite database is a local file that will save data from item resources data sent, allowing you to read the data within that file as well.
This repo is up-to-date with FastAPI.

## How to run locally:
1. Clone the repo
2. Create a virtual environment and make sure to run this command: source .venv/bin/activate
3. Run pip install on the requirements.txt file with this command: pip install -r requirements.txt
4. Make sure that all necessary requirements from pip are working
5. Run command: fastapi dev app/main.py
6. Within terminal, open the link to API docs. From there, you should be able to create, read, update, and delete!
NOTE: To view db file, you would want a program that is able to read databases. I used DBCode on VSCode to see if it was working.

## Main Python File
The main python file handles the lifespan of the application, the 

## Models Python File

