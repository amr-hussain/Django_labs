from django.db import models

# Create your models here.

class Trainee(models.Model):

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    # addding the personal photo to the root dir of media "media/trainee_photos"
    photo=models.ImageField(upload_to='trainee_photos')
    # adding a flag for activation 
    deleted=models.BooleanField(default=False)

