from django.http import HttpResponse
from django.shortcuts import render
from .models import Trainee
from django.shortcuts import redirect 
from .forms import *




# implementing the add using forms.form
def trainee_add(request):
    if request.method == "POST":
        form = add_trainee_form(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            photo = form.cleaned_data["photo"]
            course = form.cleaned_data["course"]

    
            trainee = Trainee(name=name, email=email, phone=phone, photo=photo, course=course)
            trainee.save()
            return redirect('main') 
    else:
        form = add_trainee_form()

    return render(request, "trainee/add_trainee.html", {"form": form})



def trainee_delete(request, trainee_id):
    trainee = Trainee.objects.get(id=trainee_id)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "YES":
            trainee.deleted = True
            trainee.save()
            return redirect('main')
        elif action == "NO":
            return redirect('main')

    return render(request, "trainee/delete_trainee.html", context={"trainee": trainee})

# using forms.ModelForm


def trainee_update(request, trainee_id):
    trainee = Trainee.objects.get(id=trainee_id)
    if request.method == "POST":
        form = update_trainee_form(request.POST, request.FILES, instance=trainee)
        if form.is_valid():
            form.save() 
            return redirect('main')

    else:
        form = update_trainee_form(instance=trainee)  # instance = trainee to pre-fill fomr with existing trainee data
    context = {"form": form, "trainee": trainee}
    return render(request, "trainee/update_trainee.html", context)


def trainee_list(request):
    # return HttpResponse("<h1> yes this is working </h1>")
    trainees = Trainee.objects.filter(deleted=False)
    return render(request, "trainee/trainee_list.html", context= {"trainees": trainees})
