# Generated by Django 2.0 on 2020-06-13 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='patients_account_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.IntegerField(default=0, unique=True)),
                ('bank_name', models.CharField(default='NULL', max_length=250)),
                ('date_of_debit', models.DateField(auto_now_add=True)),
                ('patient_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Patient.patients')),
            ],
        ),
    ]
