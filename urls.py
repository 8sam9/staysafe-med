from django.urls import path, include
from staysafemed.views import *


urlpatterns = [
    path('patients/', include([
        path('', PatientsDoctorListView.as_view(), name='doctor.patients.list'),
        path('<int:id>/', PatientDoctorDetailView.as_view(), name='doctor.patients.detail')
    ])),
    path('doc/', include([
        path('login/', DoctorAuthView.as_view(), name='doctor.login'),
    ])),
    path('<str:otp>/', PatientIllnessDataView.as_view(), name='patients.insertdata')
]