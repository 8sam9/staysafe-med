from django.db import models
from datetime import datetime
from .patient import Patient


class IllnessData(models.Model):
    breath_frequency = models.DecimalField(max_digits=5, decimal_places=2)
    hear_rate = models.DecimalField(max_digits=5, decimal_places=2)
    systolic_pressure = models.DecimalField(max_digits=5, decimal_places=2)
    body_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True)
    date_create = models.DateTimeField(default=datetime.utcnow)
    date_update = models.DateTimeField(auto_now=datetime.utcnow)
    date_delete = models.DateTimeField(blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return 'Patient: {} {}'.format(
            self.patient.ssn,
            self.date_create
            )
