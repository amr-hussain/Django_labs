from django.http import HttpResponse
from django.shortcuts import render

trainee_date = {

    "trainee123": {
        "id": 123,
        "name": "ali",
        "email": "ali@gmail.com",
    },
    "trainee456": {
        "id": 456,
        "name": "amr",
        "email": "amr@gmail.com",
    }
}
def login(request):
    return HttpResponse("<h1>Hello, world. You're at the login page.</h1>")

def delete_trainee(request, trainee_id):
    for key, trainer  in trainee_date.items():
        if trainer["id"] == trainee_id:
            del trainee_date[key]
            return HttpResponse(f"<h1>deleted Trainee with id {trainee_id}</h1>")
    else:
        return HttpResponse(f"<h1>Trainee with id {trainee_id} doesn't exist in database</h1>")

def add_trainee(request):
    # from post
    return render(request, "trainee/add_trainee.html")

def update_trainee(request):
    # from post
    return render(request, "trainee/update_trainee.html")

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

def show(request):
    return render(request, "trainee/add_trainee.html")
