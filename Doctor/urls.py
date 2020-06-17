from django.conf.urls import url
from . import views

urlpatterns=[
 #   url(r'^$',views.patients_list,name="patients_list"),
   url(r'^Doctor_registration/$',views.doctors_registration,name="doctors_registration"),
   url(r'^Doctor_login/$',views.doctor_login,name="doctor_login"),
   url(r'^pending_appointments_doctor/$',views.pending_appointments_doctor,name="pending_appointments_doctor"), 
   url(r'^appointment_approve/$',views.appointment_approve,name="appointment_approve"), 
   url(r'^appointment_rejection/$',views.appointment_rejection,name="appointment_rejection"), 
    
]