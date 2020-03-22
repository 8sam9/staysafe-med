from django.urls import path

from staysafemed.views import *

urlpatterns = [
    path('patients/', PatientsDoctorView.as_view()),
    path('patients/<str:otp>/', PatientDoctorDetailView.as_view()),
    path('<str:otp>/', PatientIllnessDataView.as_view())
]