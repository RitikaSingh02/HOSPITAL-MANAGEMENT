from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.patients_list,name="patients_list"),
    url(r'^Patient_registration/$',views.patients_registration,name="patients_registration"),
    url(r'^Patient_login/$',views.patient_login,name="patient_login"),
    url(r'^view_medical_history/$',views.view_medical_history,name="view_medical_history"),
    url(r'^view_prescription/$',views.view_prescription,name="view_prescription"),
    url(r'^patient_notification/$',views.patient_notification,name="patient_notification"),
    url(r'^view_payment_details/$',views.view_payment_details,name="view_payment_details"),
    url(r'^view_appointment_dates/$',views.view_appointment_dates,name="view_appointment_dates"),
]