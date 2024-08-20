from django.db import models
# from django.utils import timezone
from course.models import Course
# from datetime import date

# Create your models here.

class Classperiod(models.Model):
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='class_periods')
    classroom = models.CharField(max_length=20)
    day_of_the_week = models.CharField(max_length=25)
    total_students = models.PositiveIntegerField()
    trainer_name = models.CharField(max_length=30)
    trainers_assistant_name = models.CharField(max_length=30)
    number_of_hours = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.classroom}"