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
        illnessdata = IllnessData.objects.all().filter(patient=patient.id)
        print(illnessdata)
        return render(request, self.template, {'patient': patient})


               

