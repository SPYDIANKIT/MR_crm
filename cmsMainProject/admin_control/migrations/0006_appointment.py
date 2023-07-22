# Generated by Django 4.2.3 on 2023-07-16 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_control', '0005_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
