from django.db import models

# Create your models here.
class Course(models.Model):
    name= models.CharField(max_length=20)
    description = models.TextField()
    location = models.TextField()
    course_type = models.CharField(max_length=20)
    course_duration = models.PositiveSmallIntegerField()
    course_level = models.CharField(max_length=20)
    course_fee = models.CharField(max_length=15)
    course_trainer= models.CharField(max_length=20)
    course_students= models.PositiveSmallIntegerField()
    course_date = models.DateField()
    def __str__(self):
        return f"{self.name} {self.description}"
