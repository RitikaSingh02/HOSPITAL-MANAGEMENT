# Generated by Django 2.0 on 2020-06-13 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_patients_account_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='medical_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Anemia', models.CharField(default='NO', max_length=250)),
                ('Asthma', models.CharField(default='NO', max_length=250)),
                ('Bronchitis', models.CharField(default='NO', max_length=250)),
                ('Chickenpox', models.CharField(default='NO', max_length=250)),
                ('Diabetes', models.CharField(default='NO', max_length=250)),
                ('Pneumonia', models.CharField(default='NO', max_length=250)),
                ('Thyroid', models.CharField(default='NO', max_length=250)),
                ('Ulcer', models.CharField(default='NO', max_length=250)),
                ('other', models.CharField(default='NA', max_length=250)),
                ('medical_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Patient.patients')),
            ],
        ),
    ]
