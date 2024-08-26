from django.db import models
# from course.models import Course
from student.models import Student

class Schoolclass(models.Model):
    class_rep = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='represented_classes')
    classroom_number = models.PositiveSmallIntegerField(default=1)
    classroom_location = models.CharField(max_length=100, default='Unknown Location')
    class_capacity = models.PositiveSmallIntegerField(default=0)
    class_code = models.AutoField(primary_key=True)
    classroom_level = models.CharField(max_length=20, default='General')
    class_names = models.CharField(max_length=100, default='Unnamed Class')
    classroom_days = models.PositiveSmallIntegerField()
    # class_course = models.ForeignKey('course.Course', on_delete=models.SET_NULL, null=True, blank=True, related_name='classes')

    def __str__(self):
        return self.classroom_number
