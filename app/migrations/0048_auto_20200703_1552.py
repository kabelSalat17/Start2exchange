# Generated by Django 2.2.13 on 2020-07-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_auto_20200703_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='wallet',
            field=models.Field(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], default=0),
        ),
    ]
