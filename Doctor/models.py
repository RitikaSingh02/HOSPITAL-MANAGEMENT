from django.db import models

class doctors(models.Model):
    DOCTOR_FIRST_NAME=models.CharField(max_length=250,default="NULL")
    DOCTOR_LAST_NAME=models.CharField(max_length=250,default="NULL")
    PASSWORD=models.CharField(max_length=250,default="NULL")
    MAIL=models.CharField(max_length=250,default="NULL")
    FATHER_NAME=models.CharField(max_length=250,default="NULL")
    MOTHER_NAME=models.CharField(max_length=250,default="NULL")
    GENDER=models.CharField(max_length=250,default="NULL")
    BLOOD_GRP=models.CharField(max_length=250,default="NULL")
    DOB=models.DateField(auto_now_add=True,auto_now=False)
    STREET_ADDRESS=models.CharField(max_length=250,default="NULL")
    CITY=models.CharField(max_length=250,default="NULL")
    STATE=models.CharField(max_length=250,default="NULL")
    POSTAL_CODE=models.CharField(max_length=250,default="NULL")
    MARITAL_STATUS=models.CharField(max_length=250,default="NULL")
    MOBILE_NO=models.CharField(max_length=20,default="NULL",unique=True)
    AADHAR_NO=models.CharField(max_length=34,default="NOT AVAILABLE",unique=True)
    QUALIFICATION=models.CharField(max_length=34,default="NOT AVAILABLE",unique=True)
    PATIENT_IMG=models.ImageField(upload_to='patient_img',blank=True)
    status=models.CharField(max_length=20,default="active")
# Create your models here.
