from django.contrib.auth.models import User


class Doctor(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.ssnid

    @property
    def ssnid(self):
        return self.username
