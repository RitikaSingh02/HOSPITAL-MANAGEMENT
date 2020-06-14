from django.db import models

class receptionists(models.Model):
    receptionist_first_name=models.CharField(max_length=200)
    receptionist_last_name=models.CharField(max_length=200)
    password=models.CharField(max_length=50,unique=True)
    status=models.CharField(max_length=50,default="active")



# Create your models here.
