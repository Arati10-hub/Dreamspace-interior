# Generated by Django 5.1.1 on 2024-11-13 06:20

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('customManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
