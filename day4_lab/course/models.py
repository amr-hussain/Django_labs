from django.db import models
# from trainee.models import Trainee
# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    label = models.CharField(max_length=20)
    # foreign key to trainee
    # trainee = models.ForeignKey(Trainee, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"ID: {str(self.id)}, Name: {self.name}"