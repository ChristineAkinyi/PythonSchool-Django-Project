# Generated by Django 5.0.6 on 2024-08-19 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("classperiod", "0008_alter_classperiod_end_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classperiod",
            name="end_time",
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name="classperiod",
            name="start_time",
            field=models.TimeField(),
        ),
    ]
