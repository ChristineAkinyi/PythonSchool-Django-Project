from rest_framework import serializers
from student.models import Student
from classperiod.models import Classperiod
from teacher.models import Teacher
from course.models import Course
from schoolclass.models import Schoolclass
from datetime import date, datetime


class SchoolclassSerializer(serializers.ModelSerializer):
    class Meta:
        model =Schoolclass
        fields= "__all__"

# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = "__all__"

# class StudentSerializer(serializers.ModelSerializer):
#     course = CourseSerializer(many=True)
#     class_enrolled = SchoolclassSerializer()
#     class Meta:
#         model = Student
#         fields = "__all__"
        # exclude = ["email"] 


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, object):
        return f"{object.first_name} {object.last_name}"
    
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'email']

class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = Course
        fields = "__all__"

class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name','teacher']

class SchoolclassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = Schoolclass
        fields = "__all__"
    
class MinimalSchoolclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schoolclass
        fields = ['id', 'name','capacity']

class ClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classperiod
        fields = "__all__"

class MinimalClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classperiod
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many = True)
    class_enrolled = SchoolclassSerializer()
    class Meta:
        model = Student
        fields = "__all__"
        # exclude = ["email"] 

class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    
    def get_age(self,object):
        if object.date_of_birth:
            today = datetime.now()
        
        if isinstance(object.date_of_birth, date) and not isinstance(object.date_of_birth, datetime):
            date_of_birth = datetime.combine(object.date_of_birth, datetime.min.time())
        else:
            date_of_birth = object.date_of_birth

            age = today - date_of_birth
            return age.days // 365
        
    class Meta:
        model = Student
        fields = ["id", "first_name", "email"]

    class ClassperiodSerializer(serializers.ModelSerializer):
        schoolclass = SchoolclassSerializer()

        class Meta:
            model = Classperiod
            fields = '__all__'

    class MinimalClassperiodSerializer(serializers.ModelSerializer):
        class Meta:
            model = Classperiod
            fields = ['id', 'name', 'start_time', 'end_time']

    # full_name = serializers.MethodField()
    # def get_full_name(Self, object):
    #     return f"{object.first_name} {object.last_name}"

    # class Meta:
    #     model = Student
    #     fields = ["id", "full_name", "email"]

    # def get_age(self, object):
    #     today = datetime.now()
    #     age = today-object.date_of_birth
    #     return age
    






