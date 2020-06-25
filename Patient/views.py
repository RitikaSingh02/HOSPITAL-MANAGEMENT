from django.shortcuts import render
from django.http import JsonResponse
from . models import patients, patients_account_details,medical_history,patient_appointment_details

import json

def patients_list(request):
    if request.method=="GET":
        
        all_patients=list(patients.objects.filter(status="active").values())
        return JsonResponse(all_patients,safe=False)

def patients_registration(request):
     if request.method=="POST":

         data=json.loads(request.body)
         PATIENT_FIRST_NAME=data['PATIENT_FIRST_NAME']
         PATIENT_LAST_NAME=data['PATIENT_LAST_NAME']
         PASSWORD=data['PASSWORD']
         MAIL=data['MAIL']
         FATHER_NAME=data['FATHER_NAME']
         MOTHER_NAME=data['MOTHER_NAME']
         GENDER=data['GENDER']
         BLOOD_GRP=data['BLOOD_GRP']
         DOB=data['DOB']
         HEIGHT=data['HEIGHT']
         WEIGHT=data['WEIGHT']
         MARITAL_STATUS=data['MARITAL_STATUS']
         MOBILE_NO=data['MOBILE_NO']
         AADHAR_NO=data['AADHAR_NO']
         STREET_ADDRESS=data['STREET_ADDRESS']
         CITY=data['CITY']
         COUNTRY=data['COUNTRY']
         STATE=data['STATE']
         POSTAL_CODE=data['POSTAL_CODE']
         Anemia=data['Anemia']
         Asthma=data['Asthma']
         Bronchitis=data['Bronchitis']
         Chickenpox=data['Chickenpox']
         Diabetes=data['Diabetes']
         Pneumonia=data['Pneumonia']
         Thyroid=data['Thyroid']
         Ulcer=data['Ulcer']
         other=data['other']

         new_patients=patients.objects.create(
         PATIENT_FIRST_NAME=PATIENT_FIRST_NAME,
         PATIENT_LAST_NAME=PATIENT_LAST_NAME,
         PASSWORD=PASSWORD,
         MAIL=MAIL,
         FATHER_NAME=FATHER_NAME,
         MOTHER_NAME=MOTHER_NAME,
         GENDER=GENDER,
         BLOOD_GRP=BLOOD_GRP,
         DOB=DOB,
         HEIGHT=HEIGHT,
         WEIGHT=WEIGHT,
         MARITAL_STATUS=MARITAL_STATUS,
         MOBILE_NO=MOBILE_NO,
         AADHAR_NO=AADHAR_NO,
         STREET_ADDRESS=STREET_ADDRESS ,
         CITY=CITY,
         COUNTRY=COUNTRY,
         STATE=STATE,
         POSTAL_CODE=POSTAL_CODE
         )
         print(new_patients.id)

         patient_medical_history=medical_history.objects.create(
         Anemia=Anemia,
         Asthma=Asthma,
         Bronchitis=Bronchitis,
         Chickenpox=Chickenpox,
         Diabetes=Diabetes,
         Pneumonia=Pneumonia,
         Thyroid=Thyroid,
         Ulcer=Ulcer,
         other=other,
         medical_id=new_patients.id
         )
         return JsonResponse("true",safe=False)

def patient_login(request):
    if request.method=="POST":
         data=json.loads(request.body)
        
         PATIENT_FIRST_NAME=data['PATIENT_FIRST_NAME']
         PATIENT_LAST_NAME=data['PATIENT_LAST_NAME']
         PASSWORD=data['PASSWORD']
         patient=patients.objects.filter(PATIENT_FIRST_NAME__contains=PATIENT_FIRST_NAME,PATIENT_LAST_NAME__contains=PATIENT_LAST_NAME,
         PASSWORD__contains=PASSWORD).filter(PATIENT_FIRST_NAME=PATIENT_FIRST_NAME,
         PATIENT_LAST_NAME=PATIENT_LAST_NAME,
         PASSWORD=PASSWORD).values()
         
         if(patient):
             return JsonResponse(list(patient),safe=False)
         else:
             return JsonResponse("wrong",safe=False)



def view_medical_history(request):
    if request.method=="POST":
        data=json.loads(request.body)
        patient=medical_history.objects.filter(medical_id=data['id']).values()

        return JsonResponse(list(patient),safe=False)

def view_appointment_dates(request):
    if request.method=="POST":
        data=json.loads(request.body)
        date=patient_appointment_details.objects.filter(patient_appointment_id=data['id']
        ,appointment_date=data['appointment_date']).exclude(prescription="NA").values("appointment_date")
        return JsonResponse(list(date),safe=False)

def view_prescription(request):
    if request.method=="POST":
        data=json.loads(request.body)
        prescription=patient_appointment_details.objects.filter(patient_appointment_id=data['id'],
        appointment_date=data['appointment_date']).values("appointment_date",
        "appointment_time",
        "doctor_name",
        "doctor_id",
        "problem",
        "prescription",
        )
        
        return JsonResponse(list(prescription),safe=False)



def patient_notification(request):
    if request.method=="POST":
        data=json.loads(request.body)
        patient_notify=patient_appointment_details.objects.filter(patient_appointment_id=data['id']).values(
            "appointment_date",
            "appointment_time",
            "notification"
        )
        return JsonResponse(list(patient_notify),safe=False)

def view_payment_details(request):
    if request.method=="POST":
        data=json.loads(request.body)
        payment=patients_account_details.objects.filter(patient_id=data['id']).values('appointment_id__appointment_date',
        'appointment_id__appointment_time','date_of_debit','account_no','bank_name')
        return JsonResponse(list(payment),safe=False)



