from django.urls import path

from staysafemed.views import *

urlpatterns = [
    path('<str:otp>/', PatientView.as_view())
]