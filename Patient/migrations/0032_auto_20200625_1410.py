# Generated by Django 2.0 on 2020-06-25 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0031_auto_20200625_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients_account_details',
            old_name='patient_id',
            new_name='patient',
        ),
    ]
