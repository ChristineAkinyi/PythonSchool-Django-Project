from rest_framework import serializers
from student.models import Student
from classperiod.models import Classperiod
from teacher.models import Teacher
from course.models import Course
from schoolclass.models import Schoolclass
from datetime import date, datetime
# Teacher Serializers
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'email']
# Course Serializers
class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = Course
        fields = "__all__"
class MinimalCourseSerializer(serializers.ModelSerializer):
    teacher = MinimalTeacherSerializer()
    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher']
# Schoolclass Serializers
class SchoolclassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = Schoolclass
        fields = "__all__"
class MinimalSchoolclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schoolclass
        fields = ['id', 'name', 'capacity']
# Student Serializers
class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)
    class_enrolled = SchoolclassSerializer()
    class Meta:
        model = Student
        fields = "__all__"
class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    def get_age(self, obj):
        if obj.date_of_birth:
            today = datetime.now()
            if isinstance(obj.date_of_birth, date) and not isinstance(obj.date_of_birth, datetime):
                date_of_birth = datetime.combine(obj.date_of_birth, datetime.min.time())
            else:
                date_of_birth = obj.date_of_birth
            age = today - date_of_birth
            return age.days // 365
        return None
    class Meta:
        model = Student
        fields = ["id", "full_name", "email", "age"]
# Classperiod Serializers
class ClassperiodSerializer(serializers.ModelSerializer):
    schoolclass = SchoolclassSerializer()
    class Meta:
        model = Classperiod
        fields = "__all__"
class MinimalClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classperiod
        fields = ['id', 'name', 'start_time', 'end_time']







