from django.db import models
# from student.models import Student;

class Schoolclass(models.Model):
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE, default=1)
    classroom_number = models.PositiveSmallIntegerField(default='1')
    class_representative = models.CharField(max_length=20, default='N/A')
    classroom_location = models.CharField(max_length=20, default='akirachix')
    class_capacity = models.PositiveSmallIntegerField(default=0)
    class_code = models.AutoField(primary_key=True,default=0)
    classroom_level = models.CharField(max_length=20, default='level')
    class_names = models.CharField(max_length=15,default='class_name')
    classroom_days = models.PositiveSmallIntegerField(default='0')
    classroom_course = models.CharField(max_length=25, default='classroom_course')
    def __str__(self):
        return f"{self.class_name}"








