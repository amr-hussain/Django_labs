from django.shortcuts import render
from .models import trainee

# Create your views here.

def trainee_list(request):
    trainees = trainee.objects.all()
    return render(request, 'trainee/list.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        trainee.objects.create(name=name, email=email)
    return render(request, 'trainee/add.html')

def update_trainee(request, id):
    t = trainee.objects.get(id=id)
    if request.method == 'POST':
        t.name = request.POST['name']
        t.email = request.POST['email']
        t.save()
    return render(request, 'trainee/edit.html', {'trainee': trainee})

