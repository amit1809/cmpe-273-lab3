# cmpe-273-lab3

Lab 3
Pre-requisites
Install Pipenv
pip install pipenv
Install Flask
pipenv install flask==1.1.1
Install Ariadne for handling GraphQL schema and binding.
pipenv install ariadne==0.10.0
Create a schema.py and add this code:
TBD
Create a file called app.py and add this code snippet.
from flask import Flask, escape, request

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
Run your Hello World Flask application from a shell/terminal.
pipenv shell
$ env FLASK_APP=app.py flask run
Open this URL in a web browser or run this CLI to see the output.
curl -i http://127.0.0.1:5000/
Requirements
You will be building a RESTful class registration API in this lab.

Domain Model
|-------|               |---------|
| Class |* ---------- * | Student |
|-------|               |---------|
GraphQL operations to be implemented.
Mutate a new student
{
    "name": "Bob Smith"
}
Quety an existing student
Request

{
  students(id:1238125) {
    name
  }
}
Response

{
    "name" : "Bob Smith"
}
Mutate a class
TBD
Query a class
{
  classess(id:1238125) {
    name
    students
  }
}
Add students to a class
TBD
