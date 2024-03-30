# Generated by Django 5.0.1 on 2024-02-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('license_front', models.ImageField(upload_to='license_images/')),
                ('license_back', models.ImageField(upload_to='license_images/')),
            ],
        ),
    ]