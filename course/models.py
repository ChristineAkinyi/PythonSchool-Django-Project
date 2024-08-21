from django.db import models
from teacher.models import Teacher


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    
    # Default values added where appropriate
    syllabus = models.CharField(max_length=200, default='No syllabus provided')
    name = models.CharField(max_length=100, default='Unnamed Course')
    department = models.CharField(max_length=100, default='General Studies')
    prerequisites = models.TextField(blank=True, null=True, default='None')
    description = models.TextField(blank=True, null=True, default='No description provided')
    # teacher = models.ForeignKey('teacher.Teacher', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    trimester = models.PositiveSmallIntegerField(default=1)  # Assuming default is the first trimester
    course_head = models.CharField(max_length=100, default='Not Assigned')
    enrollment_limit = models.IntegerField(default=30)  # Assuming a default enrollment limit of 30
    class_room = models.ManyToManyField('schoolclass.Schoolclass', related_name='class_room', blank=True)
    
    def __str__(self):
        return self.name
