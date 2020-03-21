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

    def __str__(self):
        return self.ssn


class IllnessStatusHasPatient(models.Model):
    illness_status = models.ForeignKey(IllnessStatus, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_update = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return 'Patient: {} - Status: {}'.format(
            self.patient.ssn,
            self.illness_status.get_illnessStatus_display()
        )


class HospitalHasPatient(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_hospitalized = models.DateTimeField()

    def __str__(self):
        return 'Hospital: {} - Patient: {}'.format(
            self.hospital.name,
            self.patient.ssn
        )
