from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.receptionists_list,name="receptionists_list"),
    url(r'^Receptionist_login/$',views.receptionist_login,name="receptionist_login"),
    url(r'^pending_appointments/$',views.pending_appointments,name="pending_appointments"),

    
]