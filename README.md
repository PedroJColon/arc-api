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
The main python file handles the lifespan of the application and the CRUD operations needed to create, read, update, anddelete.

lifespan - Handles the lifespan of the application. If there is no database, it will create and read from that database. If there is, it will simply read the database.

create_item = Create a unique item that will be added to the database. Uses post.

read_items = Read all items within the database file. Uses get.

read_selected_item = Read a item based on item_id given. Uses get.

delete_item = Delete item based on item_id given. Uses delete.

update_item = Update item with new json data by giving a item_id to apply those changes to. Uses patch.

## Models Python File
Models.py holds the structure of the models objects, data that is important for the item to have like name, price, in_stock and description. Item ID is setup after the item is made, which becomes the public key needed to read the item.

ItemBase - The base for the item data.

Item - Extends ItemBase to give ID number for easy access of Item.

ItemUpdate - Handles new data to replace the old data.

## Test Main File
test_main.py is a unit test file to test out the API via small unit test to see if any error could occur.

## Limitations
As of now, it is currently limited to simply text for items. No images, no GUI connected, just a simple API connection. Overtime, having a GUI app connect to the API and doing CRUD operations via the GUI will be a goal that would make the app much more accessible to more people.



