# Generated by Django 5.0.6 on 2024-07-14 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
        ('student', '0004_student_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='class_id',
        ),
        migrations.AddField(
            model_name='class',
            name='student_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]
