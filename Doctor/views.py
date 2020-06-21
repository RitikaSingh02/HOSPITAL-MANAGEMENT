from django.shortcuts import render
from django.http import JsonResponse
from . models import doctors
from Patient.models import patients,patient_appointment_details
import json

def doctors_registration(request):
    if request.method=="POST":
        data=json.loads(request.body)
        doctors.objects.create(**data)
        return JsonResponse("successfully registered",safe=False)

def doctor_login(request):
    if request.method=="POST":
         data=json.loads(request.body)
        
         DOCTOR_FIRST_NAME=data['PATIENT_FIRST_NAME']
         DOCTOR_LAST_NAME=data['PATIENT_LAST_NAME']
         PASSWORD=data['PASSWORD']
         doctor=doctors.objects.filter(DOCTOR_FIRST_NAME__contains=DOCTOR_FIRST_NAME,DOCTOR_LAST_NAME__contains=DOCTOR_LAST_NAME,
         PASSWORD__contains=PASSWORD).filter(DOCTOR_FIRST_NAME=DOCTOR_FIRST_NAME,DOCTOR_LAST_NAME=DOCTOR_LAST_NAME,
         PASSWORD=PASSWORD).values()
         if(doctor):
             return JsonResponse(list(doctor),safe=False)
         else:
             return JsonResponse("not registered yet",safe=False)

def pending_appointments_doctor(request):
    if request.method=="GET":

        patient=patients.objects.filter(APPOINTMENT_STATUS_RECEPTIONIST="APPROVED",status='active').values('PATIENT_FIRST_NAME',
        'PATIENT_LAST_NAME',"patient_appointment_details__appointment_date","patient_appointment_details__appointment_time",
        "id").order_by("patient_appointment_details__id")
        
        
        return JsonResponse(list(patient),safe=False)

def appointment_approve(request):
    if request.method=="POST":#request id of the patient
        data=json.loads(request.body)
        patient=patients.objects.filter(id=data['id']).update(APPOINTMENT_STATUS_DOCTOR="APPROVED")
        patient_appointment_details.objects.filter(id=data['id']).update(reason_of_rejection="NO")
        return JsonResponse("your request has been approved by the doctor",safe=False)

def appointment_rejection(request):
    if request.method=="POST":#request id of the patient
        data=json.loads(request.body)
        patients.objects.filter(id=data['id']).update(APPOINTMENT_STATUS_DOCTOR="REJECTED")
        patient_appointment_details.objects.filter(id=data['id']).update(reason_of_rejection=data['reason'])
        return JsonResponse("your request has been rejected by the doctor  ",safe=False)