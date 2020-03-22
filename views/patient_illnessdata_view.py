from django.views import View
from django.shortcuts import render
from django.http import Http404
from django.utils.decorators import method_decorator
from staysafemed.forms.illnessdata_form import IllnessDataForm 
from staysafemed.models.patient import Patient
from staysafemed.models.patient_otp import PatientOTP
from staysafemed.models.illnessdata import IllnessData
from functools import wraps


## to be moved 
def validateOTP(func):
    @wraps(func)
    def validatePatientOTP(self, request, *args, **kwargs):
        try:
            patient_otp = PatientOTP.objects.get(otp=kwargs['otp'])
            kwargs['patientOTP'] = patient_otp
        except PatientOTP.DoesNotExist:
            raise Http404("No matches the given query.")  
        return func(self, request, *args, **kwargs)

    return validatePatientOTP


class PatientIllnessDataView(View): 
    form_class = IllnessDataForm
    template = 'patient/add_illness_data.html'
    template_success = 'patient/success_illness_data.html'

    @validateOTP
    def get(self, request, *args, **kwargs):
        patient_otp = kwargs['patientOTP']
        patient = Patient.objects.get(pk=patient_otp.patient.id)    
        return render(request, self.template, {'form': IllnessDataForm, 'patient': patient})

    @validateOTP       
    def post(self, request, *args, **kwargs):
        illnessData = IllnessData(patient=kwargs['patientOTP'].patient)
        form = self.form_class(request.POST, instance=illnessData)
        if form.is_valid():
            form.save()
            return render(request, self.template_success, {'form': form})

        return render(request, self.template, {'form': form})
            