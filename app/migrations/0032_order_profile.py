# Generated by Django 2.2.13 on 2020-06-30 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_remove_order__id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ManyToManyField(default='', to='app.Profile'),
        ),
    ]
