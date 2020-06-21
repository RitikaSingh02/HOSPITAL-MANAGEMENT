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
        password=password).values()
        if(receptionist!="NULL"):
            return JsonResponse("success",safe=False)
        else:
            return JsonResponse("failed",safe=False)

def view_doctors(request):
    if request.method=="GET":
        doctor = doctors.objects.filter(status="active").annotate(patient_count=Count('patient_appointment_details__doctor_id')).values(
            'id','DOCTOR_FIRST_NAME','DOCTOR_LAST_NAME',
        'SPECIALISATION',
        'patient_count'
        )
        return JsonResponse(list(doctor),safe=False)

def view_patients(request):
    if request.method=="POST":
        data=json.loads(request.body)
        d_id=data['id']
        doctor=patient_appointment_details.objects.filter(doctor_id=d_id).values('patient_appointment_id_id__PATIENT_FIRST_NAME',
        'patient_appointment_id_id__PATIENT_LAST_NAME')
        
        return JsonResponse(list(doctor),safe=False)


def pending_appointments(request):
    if request.method=="GET":

        patient=patients.objects.filter(APPOINTMENT_STATUS_RECEPTIONIST="PENDING",status='active').values('PATIENT_FIRST_NAME',
        'PATIENT_LAST_NAME',"patient_appointment_details__appointment_date","patient_appointment_details__appointment_time",
        "id","patient_appointment_details__speciality","patient_appointment_details__preferred_location",
        "patient_appointment_details__problem").order_by("patient_appointment_details__appointment_date")
        # patient1=patient_appointment_details.objects.filter(patient_appointment_id_id=8).values('patient_appointment_id_id__PATIENT_FIRST_NAME')
        # print(patient1)
        return JsonResponse(list(patient),safe=False)

def approve_appointment(request):
    if request.method=="POST":
        data=json.loads(request.body)
        patient=patients.objects.filter(id=data['id']).update(APPOINTMENT_STATUS_RECEPTIONIST="APPROVED",
        APPOINTMENT_STATUS_DOCTOR="PENDING")
        patient_appointment_details.objects.filter(patient_appointment_id_id=data['id']).update(doctor_name=data['doctor'],doctor_id=data['doctor_id'],
        reason_of_rejection="NO")
        return JsonResponse("your request has been approved by the manager",safe=False)

def reject_appointment(request):
    if request.method=="POST":#u have to request id and the message for rejection 
        data=json.loads(request.body)
        patient=patients.objects.filter(id=data['id']).update(APPOINTMENT_STATUS_RECEPTIONIST="REJECTED")
        patient_appointment_details.objects.filter(id=data['id']).update(reason_of_rejection=data['reason'])
        return JsonResponse("your request has been rejected by the manager",safe=False)

def update_appointment(request):
    if request.method=="POST":
        data=json.loads(request.body)
        patient=patients.objects.filter(id=data['id']).update(APPOINTMENT_STATUS_RECEPTIONIST="UPDATED")
        patient_appointment_details.objects.filter(id=data['id']).update(reason_of_rejection='UPDATED APPOINTMENT REQUIREMENTS',
        appointment_date=data['appointmnet_date'],
        appointment_time=data['appointment_time'],
        doctor_name=data['doctor_name'],
        doctor_id=data['doctor_id'])
        return JsonResponse("your request has been updated by the manager",safe=False)


