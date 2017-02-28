# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 15:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('sector', models.IntegerField(choices=[(0, 'Retail'), (1, 'Professional Services'), (2, 'Food & Drink'), (3, 'Entertainment')], default=0)),
                ('address', models.CharField(max_length=200)),
                ('registered_number', models.IntegerField(validators=[django.core.validators.RegexValidator('^\\d{10,10}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=15)),
                ('business', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='loan_request.Business')),
            ],
        ),
        migrations.CreateModel(
            name='LoanRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(100000)])),
                ('duration', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(365)])),
                ('approved', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='request',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='loan_request.LoanRequest'),
        ),
    ]