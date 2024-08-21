from django.urls import path
from .views import StudentListView
from .views import ClassperiodListView
from .views import CourseListView
from .views import TeacherListView
from .views import StudentDetailView
from .views import CourseDetailView
from .views import ClassperiodDetailView
from .views import SchoolclassListView
from .views import SchoolclassDetailView
from .views import WeeklyTimetableView


urlpatterns = [
    path("student/", StudentListView.as_view(), name="student_list_view"),
    path("classperiod/", ClassperiodListView.as_view(), name="classperiod_list_view"),
    path("schoolclass/",SchoolclassListView.as_view(),name="schoolclass_list_view"),
    path("course/", CourseListView.as_view(), name="course_list_view"),
    path("teacher/", TeacherListView.as_view(), name="teacher_list_view"),
    path("student/<int:id>/", StudentDetailView.as_view(), name="Student_detail_view"),
    path("course/<int:id>/", CourseDetailView.as_view(), name="Course_detail_view"),
    path("classperiod/<int:id>/", ClassperiodDetailView.as_view(), name="Classperiod_detail_view"),
    path("schoolclass/", SchoolclassDetailView.as_view(), name="schoolclass_list_view"),
    path("timetable/", WeeklyTimetableView.as_view(), name='weekly-timetable'),
    ]
