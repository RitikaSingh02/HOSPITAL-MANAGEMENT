from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^Patient_appointment/$',views.patient_appointment,name="patient_appointment"),
    
    url(r'^Doctor_list/$',views.Doctor_list,name="Doctor_list"),

    url(r'^department_list/$',views.department_list,name="department_list"),
    
]