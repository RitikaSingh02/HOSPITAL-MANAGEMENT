# Generated by Django 2.0 on 2020-06-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0005_auto_20200613_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='APPONITMENT_STATUS',
            field=models.CharField(default='NO', max_length=50),
        ),
        migrations.AddField(
            model_name='patients',
            name='PATIENT_IMG',
            field=models.ImageField(blank=True, upload_to='patient_img'),
        ),
    ]
