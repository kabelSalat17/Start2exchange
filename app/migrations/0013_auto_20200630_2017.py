# Generated by Django 2.2.13 on 2020-06-30 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_order_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='_id',
            new_name='questo',
        ),
        migrations.AlterField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.Profile', to_field='_id'),
        ),
    ]