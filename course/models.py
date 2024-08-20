# from django.db import models
# from schoolclass.models import Schoolclass
# from teacher.models import Teacher
# from datetime import date
# from datetime import time

# # Create your models here.
    
# class Course(models.Model):
#     course_name= models.CharField(max_length=60,default='course_name')
#     description = models.TextField(default='description')
#     location = models.TextField(default='location')
#     course_type = models.CharField(max_length=20, default='course_type')
#     course_duration = models.TimeField(default=time(9,0))
#     course_level = models.CharField(max_length=20, default='course_level')
#     course_fee = models.IntegerField(default=10000)
#     students = models.ManyToManyField('student.Student', related_name='courses')
#     course_trainer = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1, related_name='course')
#     course_students = models.TextField(default='course_students')
#     # course_start_date = models.DateField(("Date"),date.today)
#     course_end_date = models.DateField(default=date.today)
#     classes = models.ManyToManyField(Schoolclass, related_name='classes')
    
#     def __str__(self):
#         return f"{self.course_name} {self.description}"

from django.db import models
from schoolclass.models import Schoolclass
from teacher.models import Teacher
from student.models import Student
from datetime import time 
from datetime import date # Ensure correct import

from django.db import models
from teacher.models import Teacher
from schoolclass.models import Schoolclass

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    
    # Default values added where appropriate
    syllabus = models.CharField(max_length=200, default='No syllabus provided')
    name = models.CharField(max_length=100, default='Unnamed Course')
    department = models.CharField(max_length=100, default='General Studies')
    prerequisites = models.TextField(blank=True, null=True, default='None')
    description = models.TextField(blank=True, null=True, default='No description provided')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, default='')
    updated_at = models.DateTimeField(auto_now=True)
    trimester = models.PositiveSmallIntegerField(default=1)  # Assuming default is the first trimester
    course_head = models.CharField(max_length=100, default='Not Assigned')
    enrollment_limit = models.IntegerField(default=30)  # Assuming a default enrollment limit of 30
    classes = models.ManyToManyField(Schoolclass, related_name='classes', blank=True)
    
    def __str__(self):
        return self.name


# class Course(models.Model):
#     course_name = models.CharField(max_length=60, default='course_name')
#     description = models.TextField(default='description')
#     location = models.TextField(default='location')
#     course_type = models.CharField(max_length=20, default='course_type')
#     course_duration = models.TimeField(default=time(9, 0))
#     course_level = models.CharField(max_length=20, default='course_level')
#     course_fee = models.IntegerField(default=10000)
#     students = models.ManyToManyField(Student, related_name='enrolled_courses')  # Change related_name
#     course_trainer = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1, related_name='courses')
#     course_students = models.PositiveSmallIntegerField(default=0)
#     course_start_date = models.DateField(default=date.today)
#     course_end_date = models.DateField(default=date.today)
#     classes = models.ManyToManyField(Schoolclass, related_name='courses')

#     def __str__(self):
#         return f"{self.course_name} {self.description}"
