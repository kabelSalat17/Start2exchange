# Generated by Django 2.2.13 on 2020-06-30 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_order_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='profile',
        ),
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]
