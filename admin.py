from django.contrib import admin
from staysafemed.models import (
    IllnessStatus, Hospital, Doctor,
    Patient, HospitalHasPatient,
    IllnessStatusHasPatient, PatientOTP,
    IllnessData
)


class IllnessDataInline(admin.TabularInline):
    model = IllnessData
    extra = 0
    classes = ['collapse']


class PatientAdmin(admin.ModelAdmin):
    inlines = [
        IllnessDataInline
    ]


class DoctorAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return Doctor.objects.filter(is_staff=False)


admin.site.register(IllnessStatus)
admin.site.register(Hospital)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(HospitalHasPatient)
admin.site.register(IllnessStatusHasPatient)
admin.site.register(PatientOTP)
admin.site.register(IllnessData)
