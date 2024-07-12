from django.db import models

# Create your models here.

# class Teacher(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     gender = models.CharField(max_length=10)
#     country = models.CharField(max_length=100)
#     date_of_birth = models.DateField()
#     education_level = models.CharField(max_length=100)
#     subject_specialization = models.CharField(max_length=100)
#     bank_account_number = models.CharField(max_length=100, blank=True, null=True)
#     picture = models.ImageField()
#     bio = models.TextField(blank=True, null=True)
#     phone_number = models.CharField(max_length=15)
#     id = models.AutoField(primary_key=True)
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

class Teacher(models.Model):
    teacher_id = models.PositiveSmallIntegerField()
    teacher_first_name = models.CharField(max_length=20)
    teacher_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    photo = models.ImageField()
    experience = models.CharField(max_length=20)
    teacher_last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    salary = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.teacher_id} {self.teacher_last_name}"