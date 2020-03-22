from django.views import generic
from django.shortcuts import render
from django.http import Http404
from staysafemed.models.patient import Patient


class PatientsDoctorListView(generic.ListView):
    model = Patient
    context_object_name = 'patientsList'
    template_name = 'doctor/patients_list.html'

    def get_queryset(self):
        return sorted(Patient.objects.all(), key=lambda p: p.lastIllnessDataScore, reverse=True)


class PatientDoctorDetailView(generic.DetailView):
    model = Patient

