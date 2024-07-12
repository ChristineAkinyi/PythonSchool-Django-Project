from django.db import models

# Create your models here.

# class Class(models.Model):

#     id = models.AutoField(primary_key=True)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='classes')
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     school_year = models.IntegerField()
#     capacity = models.IntegerField()
#     room_number = models.IntegerField()
#     specialty = models.TextField(blank=True, null=True)
#     def __str__(self):
#         return self.name

class Class(models.Model):
    class_id = models.PositiveSmallIntegerField()
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
        return f"{self.class_id} {self.class_capacity}"
