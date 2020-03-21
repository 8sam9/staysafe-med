from django.db import models


class IllnessStatus(models.Model):
    illnessStatus = models.IntegerField(choices=[
        (0, "healthy"),
        (1, "ill_at_home"),
        (2, "hospitalized")
        ],
        unique=True
    )
