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
        patient=patients_account_details.objects.filter(patient_id_id=patient_id).exists()
        if(patient):
            patients_account_details.objects.filter(patient_id_id=patient_id).update(
                account_no=account_no,
                bank_name=bank_name,
                date_of_debit=timezone.now()
            )
            patients.objects.filter(id=patient_id).update(PAYMENT_STATUS="YES")
            return JsonResponse("updated",safe=False)
        else:
            patients_account_details.objects.create(
                account_no=account_no,
                bank_name=bank_name,
                patient_id_id=patient_id
            )
            patients.objects.filter(id=patient_id).update(PAYMENT_STATUS="YES")
            return JsonResponse("created",safe=False)

