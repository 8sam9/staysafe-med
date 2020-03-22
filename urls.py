from django.urls import path

from staysafemed.views import *

urlpatterns = [
    path('patients/', PatientsDoctorView.as_view()),
    path('<str:otp>/', PatientIllnessDataView.as_view())
]