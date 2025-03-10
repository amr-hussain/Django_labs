from django.db import models

# Create your models here.

class Trainee(models.Model):

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    # adding a foreign key pointing to the Course table in the course app
    course_id=models.ForeignKey('course.Course',on_delete=models.CASCADE)

