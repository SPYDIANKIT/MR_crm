# Generated by Django 4.2.3 on 2023-07-22 08:33

import admin_control.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_control', '0014_alter_deal_quantity_ordered_and_more'),
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
        migrations.AlterField(
            model_name='doctor',
            name='contact_number',
            field=models.CharField(max_length=20, validators=[admin_control.models.validate_contact_number]),
        ),
    ]
