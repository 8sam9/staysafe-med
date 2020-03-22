from django.contrib import admin
from staysafemed.models import (
    IllnessStatus, Hospital, Doctor,
    Patient, PatientInHospital,
    PatientHasIllnessStatus, PatientOTP,
    IllnessData
)


class IllnessDataInline(admin.TabularInline):
    model = IllnessData
    extra = 0
    can_delete = False
    classes = ['collapse']


class PatientHasIllnessStatusInline(admin.TabularInline):
    model = PatientHasIllnessStatus
    extra = 0
    can_delete = False
    classes = ['collapse']


class PatientAdmin(admin.ModelAdmin):
    inlines = [
        PatientHasIllnessStatusInline,
        IllnessDataInline
    ]


class DoctorAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return Doctor.objects.filter(is_staff=False)


admin.site.register(IllnessStatus)
admin.site.register(Hospital)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientInHospital)
admin.site.register(PatientHasIllnessStatus)
admin.site.register(PatientOTP)
admin.site.register(IllnessData)
