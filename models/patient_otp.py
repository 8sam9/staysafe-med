from uuid import uuid4
from django.db import models
from django.utils import timezone
from .patient import Patient


def expireDate():
    return timezone.localtime() + timezone.timedelta(days=40)


def generateOtp():
    return str(uuid4())[:8].upper()


class PatientOTP(models.Model):
    otp = models.CharField(max_length=8, blank=True, null=True, default=generateOtp) # noqa
    date_issued = models.DateTimeField(default=timezone.localtime)
    date_expire = models.DateTimeField(default=expireDate)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return 'OTP: {} - Patient: {}'.format(
            self.otp,
            self.patient.ssn
        )
