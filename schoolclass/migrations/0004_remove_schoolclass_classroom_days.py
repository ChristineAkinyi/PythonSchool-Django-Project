# Generated by Django 4.2.15 on 2024-08-23 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolclass', '0003_alter_schoolclass_classroom_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolclass',
            name='classroom_days',
        ),
    ]
