from django.shortcuts import render
from django.http import JsonResponse
from Doctor.models import doctors
from Patient.models import patients,patient_appointment_details,patients_account_details
import json
from django.utils import timezone

def patient_payment(request):
    if request.method=="POST":
        data=json.loads(request.body)
        patient_id=data['id']
        account_no=data['account_no']
        bank_name=data['bank_name']
        appointment=patient_appointment_details.objects.filter(patient_appointment_id=patient_id,APPOINTMENT_STATUS_RECEPTIONIST="APPROVED").exists()
        patient=patients_account_details.objects.filter(patient_id=patient_id).exists()
        if(patient and appointment):
            patients_account_details.objects.filter(patient_id=patient_id).update(
                account_no=account_no,
                bank_name=bank_name,
                date_of_debit=timezone.now()
            )
            patient_appointment_details.objects.filter(patient_appointment_id=patient_id).update(PAYMENT_STATUS="YES")
            return JsonResponse("updated",safe=False)
      
        if(not patient and appointment):
         
            patients_account_details.objects.create(
            account_no=account_no,
            bank_name=bank_name,
            patient_id=patient_id
               )
            patient_appointment_details.objects.filter(patient_appointment_id=patient_id).update(PAYMENT_STATUS="YES")
            return JsonResponse("created",safe=False)


        if(not patient and not appointment):
            return JsonResponse("wrong",safe=False)
  


