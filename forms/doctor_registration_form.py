from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from staysafemed.models.doctor import Doctor


class DoctorRegistrationForm(forms.Form):
    username = forms.CharField(label='Inserisci un nome utente', min_length=4, max_length=10)
    password = forms.CharField(label='Inserisci una password', widget=forms.PasswordInput)
    passwordconfirmation = forms.CharField(label='Conferma la password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        doctors = Doctor.objects.filter(username=username)
        if doctors.count():
            raise ValidationError('La username inserita è già in uso, cortesemente cambiala')
        return username

    def clean_passwordconfirmation(self):
        password = self.cleaned_data['password']
        passwordconfirmation = self.cleaned_data['passwordconfirmation']
        if not password or not password:
            raise ValidationError('Devi inserire la passowrd e la conferma della stessa')
        if password and passwordconfirmation and passwordconfirmation != password:
            raise ValidationError('Le password inserite non coincidono')
        return passwordconfirmation

    def save(self):
        doctor = Doctor.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['passwordconfirmation']
        )
        return doctor
