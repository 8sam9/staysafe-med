from django.contrib.auth.forms import AuthenticationForm
from staysafemed.models.doctor import Doctor


class DoctorAuthForm(AuthenticationForm):
    class Meta:
        model = Doctor

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
