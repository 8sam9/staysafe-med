from django.forms import ModelForm
from staysafemed.models.illnessdata import IllnessData

class IllnessDataForm(ModelForm):
    class Meta:
        model = IllnessData
        fields = ['breath_frequency','heart_rate','systolic_pressure','body_temperature','oxygen_saturation']