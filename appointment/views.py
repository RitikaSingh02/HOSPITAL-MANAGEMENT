from django.shortcuts import render
from django.http import JsonResponse
import json
from Patient.models import patients,patient_appointment_details
from Doctor.models import doctors


def Doctor_list(request):
    if request.method=="GET":
        all_doctor=list(doctors.objects.filter(status="active").values('DOCTOR_FIRST_NAME','DOCTOR_LAST_NAME'))
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
        patient=patient_appointment_details.objects.filter(patient_appointment_id_id=data['id']).values()

        if(patient):
            print("#")
            patients.objects.filter(id=data['id']).update(APPOINTMENT_STATUS_RECEPTIONIST="PENDING")
            patients.objects.filter(id=data['id']).update(APPOINTMENT_STATUS_DOCTOR="PENDING")
  
        else:
            patient=patient_appointment_details.objects.create(
            speciality=speciality,
            preferred_location=preferred_location,
            problem=problem,
            patient_appointment_id_id=id_patient
            )

            patients.objects.filter(id=data['id']).update(APPOINTMENT_STATUS_RECEPTIONIST="PENDING")
        return JsonResponse("yes",safe=False)

# Create your views here.
