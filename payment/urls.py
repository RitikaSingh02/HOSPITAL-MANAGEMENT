from django.conf.urls import url
from . import views

urlpatterns=[
 #   url(r'^$',views.patients_list,name="patients_list"),
   url(r'^patient_payment/$',views.patient_payment,name="patient_payment"),    
  # url(r'^create_new_account/$',views.create_new_account,name="create_new_account"),    
]