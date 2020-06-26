from django.shortcuts import render
from django.http import JsonResponse
import json
from django.db.models import Count,Min
from Patient.models import patients,patient_appointment_details
from Doctor.models import doctors

def department_list(request):
    if request.method=="GET":
        all_department=list(doctors.objects.filter(status="active").values('SPECIALISATION').distinct())
        return JsonResponse(all_department,safe=False)


def Doctor_list(request):
    if request.method=="POST":
        
        data=json.loads(request.body)
        SPECIALISATION=data['SPECIALISATION']
 
        all_doctor=list(doctors.objects.filter(status="active",SPECIALISATION=SPECIALISATION).values('id','DOCTOR_FIRST_NAME','DOCTOR_LAST_NAME','SPECIALISATION'))
        return JsonResponse(all_doctor,safe=False)

def patient_appointment(request):
    if request.method=="POST":
        data=json.loads(request.body)
        id_patient=data['id']
        appointment_date=data['appointment_date']
        appointment_time=data['appointment_time']
        speciality=data['speciality']
        preferred_location=data['preferred_location']
        problem=data['problem']
        patient=patient_appointment_details.objects.filter(patient_appointment_id=data['id'],
        appointment_date=appointment_date,
        problem=problem).exists()

        if(patient):


            return JsonResponse("duplicate appointment",safe=False)
  
        else:
            patient=patient_appointment_details.objects.create(
            speciality=speciality,
            preferred_location=preferred_location,
            problem=problem,
            patient_appointment_id=id_patient,
            APPOINTMENT_STATUS_RECEPTIONIST="PENDING"
            )
           
            return JsonResponse("appointment requested",safe=False)

def appointment_status(request):
    if request.method=="POST":
        data=json.loads(request.body)
        appointment=patient_appointment_details.objects.filter(id=data['id']).values('APPOINTMENT_STATUS_RECEPTIONIST',
        'PAYMENT_STATUS')
        return JsonResponse(list(appointment),safe=False)

# Create your views here.
