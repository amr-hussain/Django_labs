from django.http import HttpResponse
from django.shortcuts import render
from .models import Trainee
from django.shortcuts import redirect


# def delete_trainee(request, trainee_id):
#     for key, trainer  in trainee_date.items():
#         if trainer["id"] == trainee_id:
#             del trainee_date[key]
#             return HttpResponse(f"<h1>deleted Trainee with id {trainee_id}</h1>")
#     else:
#         return HttpResponse(f"<h1>Trainee with id {trainee_id} doesn't exist in database</h1>")

def trainee_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        photo = request.FILES.get('photo')
        trainee = Trainee(name=name, email=email, phone=phone, photo=photo)
        trainee.save()
        return redirect('main')
    else:
        return render(request, "trainee/add_trainee.html")



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

def trainee_update(request, trainee_id):
    trainee = Trainee.objects.get(id=trainee_id)

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "Save":
            trainee.name = request.POST.get('name')
            trainee.email = request.POST.get('email')
            trainee.phone = request.POST.get('phone')
            trainee.photo = request.FILES.get('photo')
            trainee.deleted = False
            trainee.save()
        return redirect('main') 
    else:
        return render(request, "trainee/update_trainee.html" ,context={"trainee": trainee})


def trainee_list(request):
    # return HttpResponse("<h1> yes this is working </h1>")
    trainees = Trainee.objects.filter(deleted=False)
    return render(request, "trainee/trainee_list.html", context= {"trainees": trainees})



#  if request.method == 'POST':
#         course_id = request.POST.get('course_id')
#         course_name = request.POST.get('course_name')
#         global course_data
#         course_data.append([course_id, course_name])
#         return HttpResponse("Course stored successfully!")
#     else:
#         return render(request, 'course/add_course.html')