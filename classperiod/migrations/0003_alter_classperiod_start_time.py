# Generated by Django 5.0.6 on 2024-07-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classperiod', '0002_alter_classperiod_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classperiod',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]