# Generated by Django 2.0 on 2020-06-13 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_auto_20200613_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='AADHAR_NO',
            field=models.CharField(default='NOT AVAILABLE', max_length=34, unique=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='MOBILE_NO',
            field=models.CharField(default='NULL', max_length=20, unique=True),
        ),
    ]