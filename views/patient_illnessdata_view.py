from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from staysafemed.forms.illnessdata_form import IllnessDataForm 
from staysafemed.models.patient import Patient
from staysafemed.models.illnessdata import IllnessData
from staysafemed.decorators import validateOTP


class PatientIllnessDataView(View): 
    form_class = IllnessDataForm
    template = 'patient/add_illness_data.html'
    template_success = 'patient/success_illness_data.html'

    @method_decorator(validateOTP)
    def get(self, request, *args, **kwargs):
        patient_otp = kwargs['patientOTP']
        patient = Patient.objects.get(pk=patient_otp.patient.id)    
        last_data_entry = IllnessData.objects.filter(patient=patient).last()
        return render(request, self.template, {'form': IllnessDataForm, 'patient': patient, 'illness_data':last_data_entry})

    @method_decorator(validateOTP)
    def post(self, request, *args, **kwargs):
        illnessData = IllnessData(patient=kwargs['patientOTP'].patient)
        form = self.form_class(request.POST, instance=illnessData)
        if form.is_valid():
            form.save()
            return render(request, self.template_success, {'form': form})

        return render(request, self.template, {'form': form})
            