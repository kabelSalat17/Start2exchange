# Generated by Django 2.2.13 on 2020-07-01 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20200701_2000'),
        ('users', '0003_auto_20200701_1956'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
