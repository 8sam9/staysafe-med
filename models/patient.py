from django.utils import timezone
from django.db import models
from .doctor import Doctor
from .illnessstatus import IllnessStatus
from .hospital import Hospital


class Patient(models.Model):
    ssn = models.CharField(max_length=45, unique=True)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    mobile_number_1 = models.CharField(max_length=30, blank=True)
    mobile_number_2 = models.CharField(max_length=30, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    illness_status = models.ForeignKey(IllnessStatus, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.ssn

    def lastIllnessData(self):
        return self.illnessdata_set.last()

    @property
    def patientFullName(self):
        return '{} {}'.format(self.last_name, self.first_name)

    @property
    def lastIllnessDataScore(self):
        illnessDataset = self.illnessdata_set.all()
        return illnessDataset.last().mews_score if illnessDataset else 0

    @property
    def currentPatientOTP(self):
        return self.patientotp_set.all().last()


class PatientInHospital(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_hospitalized = models.DateTimeField()

    def __str__(self):
        return 'Hospital: {} - Patient: {}'.format(
            self.hospital.name,
            self.patient.ssn
        )
