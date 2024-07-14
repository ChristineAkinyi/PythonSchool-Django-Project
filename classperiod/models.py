from django.db import models

# Create your models here.

class Classperiod(models.Model):
    start_time = models.DateField()
    end_time = models.DateField()
    course = models.CharField(max_length=25)
    classroom = models.CharField(max_length=20)
    day_of_the_week = models.CharField(max_length=15)
    total_students = models.PositiveIntegerField()
    trainer_name = models.CharField(max_length=30)
    trainers_assistant_name = models.CharField(max_length=30)
    number_of_hours = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.classroom}"