from django.db import models
from datetime import datetime



class IllnessData(models.Model):
    breath_frequency = models.DecimalField(max_digits=5, decimal_places=2)
    hear_rate = models.DecimalField(max_digits=5, decimal_places=2)
    systolic_pressure = models.DecimalField(max_digits=5, decimal_places=2)
    body_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True)
    date = models.DateField()
    date_create = models.DateTimeField(default=datetime.utcnow)
    date_update = models.DateTimeField(auto_now=datetime.utcnow)
    date_delete = models.DateTimeField()

    def __str__(self):
        return self.name
