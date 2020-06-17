from django.shortcuts import render
from django.http import JsonResponse
from . models import receptionists
from Patient.models import patients,patient_appointment_details
import json

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
        receptionist=receptionists.objects.filter(receptionist_first_name=receptionist_first_name,
        receptionist_last_name=receptionist_last_name,
        password=password).values()
        if(receptionist!="NULL"):
            return JsonResponse("success",safe=False)
        else:
            return JsonResponse("failed",safe=False)


def pending_appointments(request):
    if request.method=="GET":

        patient=patients.objects.filter(APPOINTMENT_STATUS_RECEPTIONIST="PENDING",status='active').values('PATIENT_FIRST_NAME',
        'PATIENT_LAST_NAME',"patient_appointment_details__appointment_date","patient_appointment_details__appointment_time",
        "id","patient_appointment_details__speciality","patient_appointment_details__preferred_location",
        "patient_appointment_details__problem").order_by("patient_appointment_details__id")
        
        
        return JsonResponse(list(patient),safe=False)

def approve_appointment(request):
    if request.method=="POST":
        data=json.loads(request.body)
        patient=patients.objects.filter(id=data['id']).update(APPOINTMENT_STATUS_RECEPTIONIST="APPROVED",
        APPOINTMENT_STATUS_DOCTOR="PENDING")
        return JsonResponse("your request has been approved by the manager",safe=False)

def reject_appointment(request):
    if request.method=="POST":#u have to request id and the message for rejection 
        data=json.loads(request.body)
        patient=patients.objects.filter(id=data['id']).update(APPOINTMENT_STATUS_RECEPTIONIST="REJECTED")
        return JsonResponse("your request has been approved by the manager because of the reason "+str(data['reason']),safe=False)

