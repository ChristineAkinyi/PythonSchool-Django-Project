# Generated by Django 5.0.6 on 2024-07-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classperiod', '0006_classperiod_end_time_alter_classperiod_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classperiod',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='classperiod',
            name='start_time',
            field=models.TimeField(),
        ),
    ]