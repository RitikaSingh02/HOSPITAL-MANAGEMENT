from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.patients_list,name="patients_list"),
    url(r'^Patient_registration/$',views.patients_registration,name="patients_registration"),
    url(r'^Patient_login/$',views.patient_login,name="patient_login"),
    url(r'^Patient_appointment/$',views.patient_appointment,name="patient_appointment"),
  #  url(r'^Patient_account_details/$',views.patients_account_details,name="patients_account_details"),
    
]