# Generated by Django 5.1.5 on 2025-01-29 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0008_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(choices=[('Pending', 'Pending')], default='Pending', on_delete=django.db.models.deletion.PROTECT, to='garage.brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='car',
            name='cat',
            field=models.ForeignKey(choices=[('Pending', 'Pending')], default='Pending', on_delete=django.db.models.deletion.PROTECT, to='garage.category', verbose_name='Category'),
        ),
    ]
