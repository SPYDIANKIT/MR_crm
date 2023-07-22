# Generated by Django 4.2.3 on 2023-07-22 08:55

import admin_control.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_control', '0018_alter_appointment_date_alter_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(validators=[admin_control.models.future_date_validator]),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(validators=[admin_control.models.future_date_validator]),
        ),
    ]
