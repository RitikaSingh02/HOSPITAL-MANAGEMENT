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
        appt_id=data['appointment_id']
                 
        patients_account_details.objects.create(
            account_no=account_no,
            bank_name=bank_name,
            patient_id=patient_id,
            appointment_id=appt_id
               )
        patient_appointment_details.objects.filter(patient_appointment_id=patient_id,patients_account_details__appointment_id=appt_id).update(PAYMENT_STATUS="YES")
        return JsonResponse("payment successfull",safe=False)
      
  



