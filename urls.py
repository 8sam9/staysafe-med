from django.urls import path

from staysafemed.views import *

urlpatterns = [
    path('', PatientView.as_view()),
]