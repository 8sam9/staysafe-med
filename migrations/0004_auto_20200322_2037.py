# Generated by Django 3.0.4 on 2020-03-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staysafemed', '0003_auto_20200322_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.DeleteModel(
            name='PatientHasIllnessStatus',
        ),
    ]
