from django.urls import path

from staysafemed.views import *

urlpatterns = [
    path('patients/', PatientsDoctorListView.as_view()),
    path('patients/<int:id>/', PatientDoctorDetailView.as_view()),
    path('<str:otp>/', PatientIllnessDataView.as_view())
]