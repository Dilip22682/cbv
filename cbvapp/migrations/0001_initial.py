# Generated by Django 5.1 on 2025-01-16 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('CEO', models.CharField(max_length=100)),
                ('date_of_origin', models.IntegerField()),
                ('origin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=110)),
                ('fuel_type', models.CharField(max_length=110)),
                ('milliage', models.IntegerField()),
                ('tank_capacity', models.PositiveIntegerField()),
                ('top_speed', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('CC', models.PositiveIntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='cbvapp.company')),
            ],
        ),
    ]
