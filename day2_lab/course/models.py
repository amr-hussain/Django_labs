from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)