from django.http import HttpResponse
from django.shortcuts import render

# def delete_trainee(request, trainee_id):
#     for key, trainer  in trainee_date.items():
#         if trainer["id"] == trainee_id:
#             del trainee_date[key]
#             return HttpResponse(f"<h1>deleted Trainee with id {trainee_id}</h1>")
#     else:
#         return HttpResponse(f"<h1>Trainee with id {trainee_id} doesn't exist in database</h1>")

def add_trainee(request):
    return render(request, "trainee/add_trainee.html")

def delete_trainee(request):
    return render(request, "trainee/delete_trainee.html")

def update_trainee(request):
    return render(request, "trainee/update_trainee.html")

def trainee_list(request):
    return render(request, "trainee/update_trainee.html")



