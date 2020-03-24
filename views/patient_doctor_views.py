from django.views import generic
from django.shortcuts import render
from django.http import Http404
from django.utils.decorators import method_decorator
from staysafemed.models.patient import Patient
from staysafemed.models.illnessdata import IllnessData
from staysafemed.decorators import authenticatedDoctor


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
        illnessdata = IllnessData.objects.filter(patient=patient)
        date_labels = [x['date_create'].date().strftime("%d/%m/%Y") for x in illnessdata.values('date_create')]
        dataset = [x['mews_score'] for x in illnessdata.values('mews_score')]
        print(date_labels)
        print(dataset)
        return render(request, self.template, {'patient': patient, 'illnessdata':illnessdata, 'date_labels':date_labels, 'dataset': dataset})


               

