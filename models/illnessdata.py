import locale
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .patient import Patient


class IllnessData(models.Model):
    breath_frequency = models.IntegerField()
    heart_rate = models.IntegerField()
    systolic_pressure = models.IntegerField()
    body_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    oxygen_saturation = models.IntegerField(blank=True, null=True)
    mews_score = models.IntegerField(default=0)
    notes = models.TextField(blank=True)
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=timezone.now)
    date_delete = models.DateTimeField(blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return 'Patient: {} - {}'.format(
            self.patient.ssn,
            self.date_create.astimezone().strftime('%c')
            )

    def __getSingleMewsScore(self, dataset, value):
        return next((data['score'] for data in dataset if data['min'] <= value < data['max']), 0) # noqa

    def __getMewsScore(self):
        breathFrenquencyRanges = [
            {"min": 0, "max": 9, "score": 2},
            {"min": 9, "max": 15, "score": 0},
            {"min": 15, "max": 21, "score": 1},
            {"min": 21, "max": 30, "score": 2},
            {"min": 30, "max": 100, "score": 3}
        ]
        heartRateRanges = [
            {"min": 0, "max": 41, "score": 2},
            {"min": 41, "max": 46, "score": 1},
            {"min": 51, "max": 101, "score": 0},
            {"min": 101, "max": 111, "score": 1},
            {"min": 111, "max": 130, "score": 2},
            {"min": 130, "max": 1000, "score": 3}
        ]
        systolicPressureRanges = [
            {"min": 0, "max": 71, "score": 3},
            {"min": 71, "max": 81, "score": 2},
            {"min": 81, "max": 101, "score": 1},
            {"min": 101, "max": 200, "score": 0},
            {"min": 200, "max": 1000, "score": 2}
        ]
        bodyTemperatureRanges = [
            {"min": 0, "max": 35.1, "score": 2},
            {"min": 35.1, "max": 38.4, "score": 0},
            {"min": 38.4, "max": 50, "score": 2}
        ]
        score = sum([
            self.__getSingleMewsScore(dataset=breathFrenquencyRanges, value=self.breath_frequency), # noqa
            self.__getSingleMewsScore(dataset=heartRateRanges, value=self.heart_rate), # noqa
            self.__getSingleMewsScore(dataset=systolicPressureRanges, value=self.systolic_pressure), # noqa
            self.__getSingleMewsScore(dataset=bodyTemperatureRanges, value=self.body_temperature), # noqa
        ])
        return score

    def save(self, *args, **kwargs):
        self.mews_score = self.__getMewsScore()
        sender = getattr(settings, 'EMAIL_HOST_USER', None)
        if sender:
            self.emailNotify()
        super().save(*args, **kwargs)

    def emailNotify(self):
        subject = 'Illness Data insert - Patient: {}'.format(
            self.patient.ssn[:8]
        )
        message = 'Mews Score: {}\n\nBreath Frequency: {}\nHeart Rate: {}\nSystolic Pressure: {}\nBody Temperature: {}\nOxygen Saturation: {}'.format( # noqa
            self.mews_score,
            self.breath_frequency,
            self.heart_rate,
            self.systolic_pressure,
            self.body_temperature,
            self.oxygen_saturation
        )
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.patient.doctor.email, ]
        send_mail(subject, message, email_from, recipient_list)
