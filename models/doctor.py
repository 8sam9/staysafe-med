from django.db import models


class Doctor(models.Model):
    name = models.CharField(verbose_name="Doctor Name", max_length=20)
    surname = models.CharField(verbose_name="Doctor Surname", max_length=20)
    password = models.CharField(max_length=40)
    email = models.EmailField(verbose_name="Doctor Email Address", blank=True, null=True) # noqa
    ssnid = models.CharField(verbose_name="Doctor Health System Id", max_length=30, unique=True) # noqa

    def __str__(self):
        return '{} {}'.format(
            self.name,
            self.surname
        )
