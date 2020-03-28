from django.views import generic
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from staysafemed.models import Doctor
from staysafemed.forms.doctor_registration_form import DoctorRegistrationForm
from staysafemed.decorators import authenticatedDoctor

class DoctorRegistrationView(generic.View):
    form_class = DoctorRegistrationForm
    template = 'doctor/doctor_create.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('doctor.signup'))
        else:
            if form.errors:
                for error in form.errors:
                    messages.error(request, form.errors[error][0])
            return render(request, self.template, {'form': form})
