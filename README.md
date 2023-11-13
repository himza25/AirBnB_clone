# AirBnB Clone Project

## Description

This project is a simple clone of the AirBnB application, focusing on the backend part. It includes a custom command-line interface for data management, and the storage system is file-based.

## Command Interpreter

The command interpreter is used to manage the whole application's data, allowing the following functions:
- Create a new object
- Retrieve an object from a file, a database, etc.
- Do operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy an object

### How to Start
To launch the command interpreter, navigate to the project folder and run:

./console.py

### How to Use

The command interpreter allows you to create, update, and destroy objects, as well as retrieve objects from a JSON file and convert them into Python objects.

Commands include:

- `create`: Creates a new object (ex: `create BaseModel`)
- `show`: Shows an object based on its ID (ex: `show BaseModel 1234-1234`)
- `destroy`: Destroys an object based on its ID (ex: `destroy BaseModel 1234-1234`)
- `all`: Shows all objects, or all objects of a type (ex: `all` or `all BaseModel`)
- `update`: Updates an object based on its ID (ex: `update BaseModel 1234-1234 email "a@b.com"`)

Type `help` for a list of commands within the interpreter.

### Examples

Creating a new BaseModel:

(hbnb) create BaseModel

Showing an existing object:

(hbnb) show BaseModel 1234-1234

Destroying an object:

(hbnb) destroy BaseModel 1234-1234

Listing all objects of type "User":

(hbnb) all User

Updating an object's attribute:

(hbnb) update BaseModel 1234-1234 email "a@b.com"

## Authors

This project is contributed to by the following individuals:
- Hamza Samari
- Anas Elbaidouri
