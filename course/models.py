from django.db import models

# Create your models here.

# class Course(models.Model):
#     id = models.AutoField(primary_key=True)
#     syllabus = models.CharField(max_length=200)
#     name = models.CharField(max_length=100)
#     department = models.CharField(max_length=100)
#     prerequisites = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     trimester = models.PositiveSmallIntegerField()
#     course_head = models.CharField(max_length=100)
#     enrollment_limit = models.IntegerField()
#     classes = models.ManyToManyField(Class, related_name='courses')
    
#     def __str__(self):
#         return self.name
    
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
