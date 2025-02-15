# Generated by Django 5.0.7 on 2024-07-31 06:57

import django.core.validators
import phonenumber_field.modelfields
import voterapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_id', models.CharField(auto_created=True, editable=False, max_length=10, unique=True)),
                ('first_name', models.CharField(max_length=45, validators=[voterapp.models.cheack])),
                ('last_name', models.CharField(max_length=45, validators=[voterapp.models.cheack])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=40)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{6}$', 'Pincode must have exactly 6 digits.')])),
                ('date_of_birth', models.DateField()),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN')),
            ],
        ),
    ]
