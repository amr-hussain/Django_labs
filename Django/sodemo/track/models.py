from django.db import models

# Create your models here.
#model Track
class Track2(models.Model):
    #prop
    #id int autoincrement pk
    id=models.AutoField(primary_key=True)
    #name varchar 50
    name=models.CharField(max_length=50)
    # col=models.CharField(max_length=255)

