from django.http import HttpResponse
from django.shortcuts import render
# import json


# json_data = "trainees.json"
#
# def load_data():
#     try:
#         with open(json_data, "r") as json_file:
#             return json.load(json_file)
#     except :
#         raise ValueError
#
# def save_data(data):
#     with open(json_data, "w") as json_file:
#         # indent 4 for readability only
#         json.dump(data, json_file, indent=4)
#

trainee_date = {

    "trainee1": {
        "id": 123,
        "name": "ali",
        "email": "ali@gmail.com",
    },
    "trainee2": {
        "id": 456,
        "name": "amr",
        "email": "amr@gmail.com",
    }
}
def login(request):
    return HttpResponse("<h1>Hello, world. You're at the login page.</h1>")

def delete_trainee(request):
    return HttpResponse("<h1>Hello, world.</h1>")
#
def list_trainees(request):
    output = "<h1>List of Trainees</h1>"
    output += "<ul>"
    for t in trainee_date.values():
        output += (f"<li>ID = {t['id']}</li> \n\
        <li style='list-style: none; padding-left: 30px;'> \
        trainee name: {t['name']}, Email: {t['email']} \
        </li>")
    output += "</ul>"

    return HttpResponse(output)


