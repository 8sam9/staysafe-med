from django.forms import ModelForm
from staysafemed.models.patient import Patient

class PatientDataForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['ssn', 'mobile_number_1', 'mobile_number_2']
