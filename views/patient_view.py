from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from staysafemed.forms.illnessdata_form import IllnessDataForm 

class PatientView(View): 
    form_class = IllnessDataForm
    template = 'patient/add_illness_data.html'
    template_success = 'patient/success_illness_data.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {'form': IllnessDataForm})   

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>          
            return render(request, self.template_success, {'form': form})

        return render(request, self.template, {'form': form})
            