from django.db import models
# from student.models import Student;

class Schoolclass(models.Model):
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE, default=1)
    # classroom_number = models.PositiveSmallIntegerField()
    classroom_trainer_name = models.CharField(max_length=20)
    classroom_location = models.CharField(max_length=20)
    classroom_capacity = models.PositiveSmallIntegerField()
    classroom_level = models.CharField(max_length=20)
    classroom_name = models.CharField(max_length=15)
    classroom_days = models.PositiveSmallIntegerField()
    classroom_student_names = models.TextField()
    classroom_course = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.classroom_name}"








