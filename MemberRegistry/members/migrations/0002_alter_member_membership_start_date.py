# Generated by Django 4.1.13 on 2024-10-29 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='membership_start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
