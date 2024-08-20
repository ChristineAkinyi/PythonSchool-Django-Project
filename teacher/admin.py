from django.contrib import admin

from.models import Teacher
admin.site.register(Teacher)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'teacher_id', 'teacher_email', 'phone_number', 'department')


# Register your models here.
