from django.urls import path, include
from staysafemed.views import *


urlpatterns = [
    path('patients/', include([
        path('', PatientsDoctorListView.as_view(), name='doctor.patients.list'),
        path('add/', PatientDoctorAddView.as_view(), name='doctor.patients.add'),
        path('<int:id>/', PatientDoctorDetailView.as_view(), name='doctor.patients.detail')
    ])),
    path('doc/', include([
        path('register/', DoctorRegistrationView.as_view(), name='doctor.signup'),
        path('login/', DoctorAuthView.as_view(), name='doctor.login'),
    ])),
    path('<str:otp>/', PatientIllnessDataView.as_view(), name='patients.insertdata')
]