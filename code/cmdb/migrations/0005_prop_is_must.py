# Generated by Django 2.0.2 on 2018-03-13 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_auto_20180313_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='prop',
            name='is_must',
            field=models.BooleanField(default=False),
        ),
    ]
