# Generated by Django 5.1.5 on 2025-01-29 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0005_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Name Category'),
        ),
    ]
