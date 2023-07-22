# Generated by Django 4.2.3 on 2023-07-22 08:34

import admin_control.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_control', '0015_alter_appointment_date_alter_appointment_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='contact_number',
            field=models.IntegerField(max_length=20, validators=[admin_control.models.validate_contact_number]),
        ),
    ]
