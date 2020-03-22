from django.views import View
from django.shortcuts import render
from staysafemed.forms.illnessdata_form import IllnessDataForm 

class PatientView(View): 
    template = 'patient/add_illness_data.html'
    form_class = IllnessDataForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {'form': IllnessDataForm})   