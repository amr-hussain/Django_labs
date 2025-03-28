from django.db import models
from course.models import Course
from django.core.files.storage import default_storage #to get and modify the file path

# Utilizing pre-built dnago authentication
from django.contrib.auth.models import User


class Trainee(models.Model):

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    # addding the personal photo to the root dir of media "media/trainee_photos"
    photo=models.ImageField(upload_to='trainee/photos')
    # adding a flag for activation 
    deleted=models.BooleanField(default=False)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)



    def __str__(self):
        return self.name 
    
    # performing method overriding on save() to add delete old image functionality
    def save(self, *args, **kwargs):
        
        # old_record = [id(pk), old_name, old_col  , , old_photo]
        # new_record = [id(pk), new_name, new_col , , new_photo]
        # we still don't know if the new photo is the same as the old photo..

        # first making sure the obj (record) has a primary key
        # which inform that this is not a new record
        if self.pk:
            old_record = Trainee.objects.get(pk=self.pk)
            # we don't have to check for old_record.photo if the column is required
            if old_record.photo and self.photo != old_record.photo:
                # to prevent raising error if the old image path was lost somehow.
                if default_storage.exists(old_record.photo.path):
                    default_storage.delete(old_record.photo.path)

        # now we append the default behavior of the save method
        super().save(*args, **kwargs)