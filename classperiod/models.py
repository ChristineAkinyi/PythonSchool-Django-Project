from django.db import models
from datetime import time

class ClassPeriod(models.Model):
    start_time = models.TimeField(null=True, blank=True, default=time(9, 0))  # 09:00:00
    end_time = models.TimeField(null=True, blank=True, default=time(17, 0))    # 17:00:00
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='class_periods')
    classroom = models.CharField(max_length=20)
    day_of_the_week = models.CharField(max_length=25)
    total_students = models.PositiveIntegerField(default=0)
    trainer_name = models.CharField(max_length=30, blank=True)
    trainers_assistant_name = models.CharField(max_length=30, blank=True)
    number_of_hours = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.course} - {self.classroom} - {self.day_of_the_week} ({self.start_time} to {self.end_time})"
