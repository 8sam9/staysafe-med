from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    referrer = models.CharField(max_length=50, blank=True, null=True)
    phone_number_1 = models.CharField(max_length=30, blank=True)
    phone_number_2 = models.CharField(max_length=30, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('city', 'name',)

    def __str__(self):
        return '{} - {}'.format(
            self.city,
            self.name
            )
