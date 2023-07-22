# Generated by Django 4.2.3 on 2023-07-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_control', '0022_appoinmentstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointmentss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scheduled_date', models.DateField()),
                ('scheduled_time', models.TimeField()),
                ('is_successful', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='appoinmentstatus',
        ),
    ]
