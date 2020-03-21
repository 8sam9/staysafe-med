from django.contrib import admin
from staysafemed.models import (
    IllnessStatus, Hospital, Doctor,
    Patient, HospitalHasPatient,
    IllnessStatusHasPatient, PatientOTP
)


admin.site.register(IllnessStatus)
admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(HospitalHasPatient)
admin.site.register(IllnessStatusHasPatient)
admin.site.register(PatientOTP)
