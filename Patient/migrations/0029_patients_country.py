# Generated by Django 2.0 on 2020-06-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0028_auto_20200623_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='COUNTRY',
            field=models.CharField(default='NULL', max_length=250),
        ),
    ]