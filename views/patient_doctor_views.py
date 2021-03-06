from django.views import generic
from django.shortcuts import render, redirect, reverse
from django.http import Http404
from django.utils.decorators import method_decorator
from staysafemed.models.patient import Patient
from staysafemed.models.patient_otp import PatientOTP
from staysafemed.models.illnessdata import IllnessData
from staysafemed.forms.patient_form import PatientDataForm
from staysafemed.decorators import authenticatedDoctor
from staysafemed.models.dataset import IllnessDataSet
import json
from django.core.serializers.json import DjangoJSONEncoder



class PatientsDoctorListView(generic.ListView):
    model = Patient
    context_object_name = 'patientsList'
    template_name = 'doctor/dashboard.html'

    def get_queryset(self):
        return sorted(Patient.objects.all(), key=lambda p: p.lastIllnessDataScore, reverse=True)

    @method_decorator(authenticatedDoctor)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PatientDoctorDetailView(generic.View):
    template = 'doctor/patient_detail.html'

    @method_decorator(authenticatedDoctor)
    def get(self, request, *args, **kwargs):
        try: 
            patient = Patient.objects.get(pk=kwargs['id'])
        except Patient.DoesNotExist:
            raise Http404("No matches the given query.")

        illnessdata = IllnessData.objects.filter(patient=patient).order_by('-date_create')
        date_labels = [x['date_create'].date().strftime("%d/%m") for x in illnessdata.values('date_create')]
        
        # General Dataset 

        general_datasets = [
            IllnessDataSet('breath_frequency',illnessdata, 'Frequenza di respiro',borderColor='rgb(255, 99, 132)'),
            IllnessDataSet('heart_rate',illnessdata, 'Frequenza cardiaca' , borderColor='rgb(116, 0, 0)'),
            IllnessDataSet('systolic_pressure',illnessdata, 'Pressione Sistolica' , borderColor='rgb(116, 150, 0)'),
            IllnessDataSet('body_temperature',illnessdata, 'Temperatura Corporea' , borderColor='rgb(116, 220, 0)'),
            IllnessDataSet('oxygen_saturation',illnessdata, 'Saturazione Ossigeno' ,borderColor='rgb(116, 54, 0)')
            ]
        general_chart = { 
            'date_labels': date_labels,
            'dataset' : json.dumps([dataset.__dict__ for dataset in general_datasets],cls=DjangoJSONEncoder)
        }

        # Mew Score Dataset 

        mew_score_datasets = [
            IllnessDataSet('mews_score',illnessdata, 'Mew Score' ,borderColor='rgb(206, 10, 0)',backgroundColor='rgba(206, 10, 0, 0.2)', fill=True)
        ]
        mew_score_chart = { 
            'date_labels': date_labels,
            'dataset' : json.dumps([dataset.__dict__ for dataset in mew_score_datasets],cls=DjangoJSONEncoder)
        }
        return render(request, self.template, {'patient': patient, 'illnessdata':illnessdata, 'general_chart':general_chart, 'mew_score_chart': mew_score_chart })

class PatientDoctorAddView(generic.View):
    form_class = PatientDataForm
    template = 'doctor/patient_create.html'

    @method_decorator(authenticatedDoctor)
    def get(self, request, *args, **kwargs):
        return render(request, self.template, {'form': self.form_class})

    @method_decorator(authenticatedDoctor)
    def post(self, request, *args, **kwargs):
        patient = Patient(doctor=self.request.user)
        form = self.form_class(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            patientOtp = PatientOTP(patient=patient)
            patientOtp.save()
            return redirect(reverse('doctor.patients.list'))

        return render(request, self.template, {'form': self.form_class})

