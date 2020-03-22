from django.views import generic
from django.contrib.auth.views import LoginView
from staysafemed.models import Doctor
from staysafemed.forms.doctor_auth_form import DoctorAuthForm


class DoctorAuthView(LoginView):
    form_class = DoctorAuthForm
    template = 'doctor/login.html'
    template_name = 'admin/login.html'
