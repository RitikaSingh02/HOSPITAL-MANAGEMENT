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
        
         DOCTOR_FIRST_NAME=data['DOCTOR_FIRST_NAME']
         DOCTOR_LAST_NAME=data['DOCTOR_LAST_NAME']
         PASSWORD=data['PASSWORD']
         doctor=doctors.objects.filter(DOCTOR_FIRST_NAME__contains=DOCTOR_FIRST_NAME,DOCTOR_LAST_NAME__contains=DOCTOR_LAST_NAME,
         PASSWORD__contains=PASSWORD).filter(DOCTOR_FIRST_NAME=DOCTOR_FIRST_NAME,DOCTOR_LAST_NAME=DOCTOR_LAST_NAME,
         PASSWORD=PASSWORD).values()
         if(doctor):
             return JsonResponse(list(doctor),safe=False)
         else:
             return JsonResponse("wrong",safe=False)

def pending_appointments_doctor(request):
    if request.method=="POST":
        data=json.loads(request.body)
        patient=patient_appointment_details.objects.filter(PAYMENT_STATUS="YES",
        doctor_id=data['id'],APPOINTMENT_STATUS_DOCTOR="PENDING").values('patient_appointment_id__PATIENT_FIRST_NAME',
        'patient_appointment_id__PATIENT_LAST_NAME',"appointment_date",      
        "appointment_time",
        "problem",
        "patient_appointment_id").order_by("appointment_date")
        
        
        return JsonResponse(list(patient),safe=False)

def appointment_approve(request):
    if request.method=="POST":#request id of the patient
        data=json.loads(request.body)
        
        patient_appointment_details.objects.filter(patient_appointment_id=data["patient_appointment_id"],appointment_date=data['appointment_date'],problem=data['problem']).update(APPOINTMENT_STATUS_DOCTOR="APPROVED",
        notification="APPROVED BY THE DOCTOR")
        return JsonResponse("your request has been approved by the doctorl",safe=False)

def appointment_rejection(request):
    if request.method=="POST":#request id of the patient
        data=json.loads(request.body)
       
        patient_appointment_details.objects.filter(patient_appointment_id=data['id'],appointment_date=data['appointment_date']).update(APPOINTMENT_STATUS_DOCTOR="REJECTED",
        notification='REQUEST WAS REJECTED BY THE DOCTOR '+data['reason'])
        return JsonResponse("your request has been rejected by the doctor",safe=False)
    
def view_patients(request):
    if request.method=="POST":
        data=json.loads(request.body)
        d_id=data['id']
        doctor=patient_appointment_details.objects.filter(doctor_id=d_id,APPOINTMENT_STATUS_DOCTOR="APPROVED").values(
        'patient_appointment_id',
        'patient_appointment_id__PATIENT_FIRST_NAME',
        'patient_appointment_id__PATIENT_LAST_NAME').distinct()
        
        return JsonResponse(list(doctor),safe=False)

def view_approved_appointments(request):
    if request.method=="POST":
        data=json.loads(request.body)
        d_id=data['id']
        doctor=patient_appointment_details.objects.filter(doctor_id=d_id,APPOINTMENT_STATUS_DOCTOR="APPROVED").values(
        'patient_appointment_id',
        'patient_appointment_id__PATIENT_FIRST_NAME',
        'patient_appointment_id__PATIENT_LAST_NAME',
        'problem')
        
        return JsonResponse(list(doctor),safe=False)

def prescription(request):
    if request.method=="POST":
        data=json.loads(request.body)
        patient_id=data['id']
        patient_appointment_details.objects.filter(patient_appointment_id=patient_id,
        appointment_date=data['appointment_date']).update(prescription=data['prescription'])
        return JsonResponse("success",safe=False)
    

