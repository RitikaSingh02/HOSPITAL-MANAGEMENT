from django.db import models
from datetime import datetime,date 
from Doctor.models import doctors

class patients(models.Model):
    PATIENT_FIRST_NAME=models.CharField(max_length=250,default="NULL")
    PATIENT_LAST_NAME=models.CharField(max_length=250,default="NULL")
    PASSWORD=models.CharField(max_length=250,default="NULL")
    MAIL=models.CharField(max_length=250,default="NULL")
    FATHER_NAME=models.CharField(max_length=250,default="NULL")
    MOTHER_NAME=models.CharField(max_length=250,default="NULL")
    GENDER=models.CharField(max_length=250,default="NULL")
    BLOOD_GRP=models.CharField(max_length=250,default="NULL")
    DOB=models.DateField(auto_now_add=True,auto_now=False)
    HEIGHT=models.IntegerField(default=0)
    WEIGHT=models.IntegerField(default=0)
    STREET_ADDRESS=models.CharField(max_length=250,default="NULL")
    CITY=models.CharField(max_length=250,default="NULL")
    STATE=models.CharField(max_length=250,default="NULL")
    COUNTRY=models.CharField(max_length=250,default="NULL")
    POSTAL_CODE=models.CharField(max_length=250,default="NULL")
    MARITAL_STATUS=models.CharField(max_length=250,default="NULL")
    MOBILE_NO=models.CharField(max_length=20,default="NULL")
    AADHAR_NO=models.CharField(max_length=34,default="NOT AVAILABLE",unique=True)
    PATIENT_IMG=models.ImageField(upload_to='patient_img',blank=True)
    status=models.CharField(max_length=20,default="active")

    
class patient_appointment_details(models.Model):
    patient_appointment=models.ForeignKey(patients,null=True,on_delete=models.SET_NULL)
    APPOINTMENT_STATUS_RECEPTIONIST=models.CharField(max_length=50,default="NO")
    APPOINTMENT_STATUS_DOCTOR=models.CharField(max_length=50,default="NOT PROCEEDED")
    appointment_date=models.DateField(auto_now_add=True,auto_now=False)
    appointment_time=models.TimeField(auto_now=True,auto_now_add=False)
    speciality=models.CharField(max_length=250,default="NULL")
    preferred_location=models.CharField(max_length=250,default="NULL")
    problem=models.CharField(max_length=250,default="NULL")
    doctor_name=models.CharField(max_length=250,default="NULL")
    doctor=models.ForeignKey(doctors,null=True,on_delete=models.SET_NULL)
    notification=models.CharField(max_length=250,default="NULL")
    prescription=models.CharField(max_length=250,default="NA")
    PAYMENT_STATUS=models.CharField(max_length=50,default="NO")

class patients_account_details(models.Model):
    patient=models.ForeignKey(patients,null=True,on_delete=models.SET_NULL)
    appointment=models.ForeignKey(patient_appointment_details,null=True,on_delete=models.SET_NULL)
    account_no=models.BigIntegerField(default=0)
    bank_name=models.CharField(max_length=250,default="NULL")
    date_of_debit=models.DateField(auto_now_add=True,auto_now=False)

class medical_history(models.Model):
    medical=models.ForeignKey(patients,null=True,on_delete=models.SET_NULL)
    Anemia=models.CharField(max_length=250,default="NO")
    Asthma=models.CharField(max_length=250,default="NO")
    Bronchitis=models.CharField(max_length=250,default="NO")
    Chickenpox=models.CharField(max_length=250,default="NO")
    Diabetes=models.CharField(max_length=250,default="NO")
    Pneumonia=models.CharField(max_length=250,default="NO")
    Thyroid=models.CharField(max_length=250,default="NO")
    Ulcer=models.CharField(max_length=250,default="NO")
    other=models.CharField(max_length=250,default="NA")
    



# Create your models here.
