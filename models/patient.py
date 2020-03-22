import locale
from django.utils import timezone
from django.db import models
from django.conf import settings
from .doctor import Doctor
from .illnessstatus import IllnessStatus
from .hospital import Hospital

LC = settings.LANGUAGE_CODE
LC_ALL = '{}_{}.UTF-8'.format(LC.lower(), LC.upper())


class Patient(models.Model):
    ssn = models.CharField(max_length=45, unique=True)
    mobile_number_1 = models.CharField(max_length=30, blank=True)
    mobile_number_2 = models.CharField(max_length=30, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    illness_status = models.ManyToManyField(IllnessStatus, through='PatientHasIllnessStatus') # noqa

    def __str__(self):
        return self.ssn

    @property
    def lastIllnessDataScore(self):
        illnessDataset = self.illnessdata_set.all()
        return illnessDataset.last().mews_score if illnessDataset else 0

    @property
    def currentPatientOTP(self):
        return self.patientotp.all().last()


class PatientHasIllnessStatus(models.Model):
    illness_status = models.ForeignKey(IllnessStatus, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_update = models.DateTimeField(auto_now=timezone.localtime)

    def __str__(self):
        locale.setlocale(locale.LC_ALL, LC_ALL)
        return 'Patient: {} - Status: {} - Date: {}'.format(
            self.patient.ssn,
            self.illness_status.get_illnessStatus_display(),
            self.date_update.astimezone().strftime('%c')
        )


class PatientInHospital(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_hospitalized = models.DateTimeField()

    def __str__(self):
        return 'Hospital: {} - Patient: {}'.format(
            self.hospital.name,
            self.patient.ssn
        )
