from functools import wraps
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from staysafemed.models.patient_otp import PatientOTP

def validateOTP(func):
    @wraps(func)
    def validatePatientOTP(self, request, *args, **kwargs):
        try:
            patient_otp = PatientOTP.objects.get(otp=kwargs['otp'])
            kwargs['patientOTP'] = patient_otp
        except PatientOTP.DoesNotExist:
            raise Http404("No matches the given query.")  
        return func(self, request, *args, **kwargs)

    return validatePatientOTP

def authenticatedDoctor(func):
    return login_required(func, login_url='/doc/login/')
