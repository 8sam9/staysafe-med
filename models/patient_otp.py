from django.db import models
from uuid import uuid4
from datetime import datetime, timedelta
from .patient import Patient


def expireDate():
    return datetime.utcnow() + timedelta(days=40)


def generateOtp():
    return str(uuid4())[:8].upper()


class PatientOTP(models.Model):
    otp = models.CharField(max_length=8, blank=True, null=True, default=generateOtp) # noqa
    date_issued = models.DateTimeField(default=datetime.utcnow)
    date_expire = models.DateTimeField(default=expireDate)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
