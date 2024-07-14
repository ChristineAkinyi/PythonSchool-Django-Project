from django.db import models
from student.models import Student;

# Create your models here.

class Class(models.Model):
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE, default=1)
    # class_id = models.PositiveSmallIntegerField()
    class_number = models.PositiveSmallIntegerField()
    class_trainer_name = models.CharField(max_length=20)
    class_location = models.CharField(max_length=20)
    class_capacity = models.PositiveSmallIntegerField()
    class_level = models.CharField(max_length=20)
    class_name = models.CharField(max_length=15)
    class_days = models.PositiveSmallIntegerField()
    class_student_names = models.TextField()
    class_course = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.class_number} {self.class_capacity}"
