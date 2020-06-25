from django.shortcuts import render
from django.http import JsonResponse
from . models import receptionists
from Patient.models import patients,patient_appointment_details
from Doctor.models import doctors
import json
from django.db.models import Count

def receptionists_list(request):
    if request.method=="GET":
        users=list(receptionists.objects.filter(status="active").values())
        return JsonResponse(users,safe=False)

def receptionist_login(request):
    if request.method=="POST":
        data=json.loads(request.body)
        receptionist_first_name=data['receptionist_first_name']
        receptionist_last_name=data['receptionist_last_name']
        password=data['password']
        receptionist=receptionists.objects.filter(receptionist_first_name__contains=receptionist_first_name,
        receptionist_last_name__contains=receptionist_last_name,
        password__contains=password).filter(receptionist_first_name=receptionist_first_name,
        receptionist_last_name=receptionist_last_name,
        password=password).exists()
        if(receptionist):
            return JsonResponse("success",safe=False)
        else:
            return JsonResponse("failed",safe=False)

def view_doctors(request):
    if request.method=="GET":
        doctor = doctors.objects.filter(status="active").annotate(patient_count=Count('patient_appointment_details__patient_appointment_id',distinct=True)).values(
            'id','DOCTOR_FIRST_NAME','DOCTOR_LAST_NAME',
        'SPECIALISATION',
        'patient_count'
        )
        return JsonResponse(list(doctor),safe=False)

def view_patients(request):
    if request.method=="POST":
        data=json.loads(request.body)
        d_id=data['id']
        doctor=patient_appointment_details.objects.filter(doctor_id=d_id).values(
        'patient_appointment_id',
        'patient_appointment_id__PATIENT_FIRST_NAME',
        'patient_appointment_id__PATIENT_LAST_NAME').distinct()
        
        return JsonResponse(list(doctor),safe=False)


def pending_appointments(request):
    if request.method=="GET":

        patient=patient_appointment_details.objects.filter(APPOINTMENT_STATUS_RECEPTIONIST="PENDING").values('patient_appointment_id__PATIENT_FIRST_NAME',
        'patient_appointment_id__PATIENT_LAST_NAME',"appointment_date","appointment_time",
        "patient_appointment_id","speciality","preferred_location",
        "problem").order_by("appointment_date")
        # patient1=patient_appointment_details.objects.filter(patient_appointment_id=8).values('patient_appointment_id_id__PATIENT_FIRST_NAME')
        # print(patient1)
        return JsonResponse(list(patient),safe=False)

def approve_appointment(request):
    if request.method=="POST":
        data=json.loads(request.body)
        patient_appointment_details.objects.filter(patient_appointment_id=data['id'],
        appointment_date=data['appointment_date']).update(doctor_name=data['doctor'],doctor_id=data['doctor_id'],
        APPOINTMENT_STATUS_RECEPTIONIST="APPROVED",
        APPOINTMENT_STATUS_DOCTOR="PENDING",
        notification="APPROVED BY THE MANAGER WAITING FOR THE DOCTOR")
        return JsonResponse("your request has been approved by the manager",safe=False)

def reject_appointment(request):
    if request.method=="POST":#u have to request id and the message for rejection 
        data=json.loads(request.body)
        
        patient_appointment_details.objects.filter(patient_appointment_id=data['id'],appointment_date=data['appointment_date']).update(notification="REJECTED BY THE MANAGER "+data['reason'],
        APPOINTMENT_STATUS_RECEPTIONIST="REJECTED")
        
        return JsonResponse("your request has been rejected by the manager",safe=False)

def update_appointment(request):
    if request.method=="POST":
        data=json.loads(request.body)
       
        patient_appointment_details.objects.filter(patient_appointment_id=data['id'],appointment_date=data['appointment_date']).update(reason_of_rejection='UPDATED APPOINTMENT REQUIREMENTS BY THE MANAGER',
        appointment_date=data['appointment_date'],
        appointment_time=data['appointment_time'],
        doctor_name=data['doctor_name'],
        doctor_id=data['doctor_id'],
        APPOINTMENT_STATUS_RECEPTIONIST="UPDATED")
        return JsonResponse("your request has been updated by the manager",safe=False)


