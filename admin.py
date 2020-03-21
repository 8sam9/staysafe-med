from django.contrib import admin
from staysafemed.models import (
    IllnessStatus, Hospital, Doctor,
    Patient, HospitalHasPatient,
    IllnessStatusHasPatient, PatientOTP
)


class DoctorAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return Doctor.objects.filter(is_staff=False)


admin.site.register(IllnessStatus)
admin.site.register(Hospital)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient)
admin.site.register(HospitalHasPatient)
admin.site.register(IllnessStatusHasPatient)
admin.site.register(PatientOTP)
