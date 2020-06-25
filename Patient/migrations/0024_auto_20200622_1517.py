# Generated by Django 2.0 on 2020-06-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0023_auto_20200622_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medical_history',
            name='prescription',
        ),
        migrations.AddField(
            model_name='patient_appointment_details',
            name='prescription',
            field=models.CharField(default='NA', max_length=250),
        ),
    ]
