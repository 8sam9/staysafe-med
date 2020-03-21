from datetime import datetime
from django.db import models
from .doctor import Doctor
from .illnessstatus import IllnessStatus
from .hospital import Hospital


class Patient(models.Model):
    ssn = models.CharField(max_length=45, unique=True)
    mobile_number_1 = models.CharField(max_length=30, blank=True)
    mobile_number_2 = models.CharField(max_length=30, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    illness_status = models.ManyToManyField(IllnessStatus, through='IllnessStatusHasPatient') # noqa


class IllnessStatusHasPatient(models.Model):
    illness_status = models.ForeignKey(IllnessStatus, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_update = models.DateTimeField(default=datetime.utcnow)


class HospitalHasPatient(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_hospitalized = models.DateTimeField()
