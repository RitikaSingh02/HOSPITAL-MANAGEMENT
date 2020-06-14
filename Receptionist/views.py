from django.shortcuts import render
from django.http import JsonResponse
from . models import receptionists
from Patient.models import patients
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

#def receptionist_dashboard(request):


def pending_appointments(request):
    if request.method=="GET":
        patients=patients.objects.filter(APPOINTMENT_STATUS="PENDING").values()
        return JsonResponse(list(patients),safe=False)
# Create your views here.
