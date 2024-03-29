# Generated by Django 4.2.3 on 2023-07-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=50)),
                ('Company_Name', models.CharField(max_length=50)),
                ('Product_Image', models.ImageField(upload_to='media')),
                ('Product_Price', models.FloatField(default=0)),
                ('Entered_By', models.CharField(max_length=50)),
            ],
        ),
    ]
