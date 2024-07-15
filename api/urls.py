from django.urls import path
from .views import StudentListView
from .views import ClassPeriodListView
from .views import CourseListView
from .views import TeacherListView
# from .views import ClassListView


urlpatterns = [
    path("student/", StudentListView.as_view(), name="student_list_view"),
    path("classperiod/", ClassPeriodListView.as_view(), name="classperiod_list_view"),
    path("course/", CourseListView.as_view(), name="course_list_view"),
    path("teacher/", TeacherListView.as_view(), name="teacher_list_view"),
    ]