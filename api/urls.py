from django.urls import path
from .views import StudentListViews
from .views import ClassperiodListViews
from .views import CourseListViews
from .views import TeacherListViews
from .views import TeacherDetailView
from .views import StudentDetailView
from .views import CourseDetailView
from .views import ClassperiodDetailView
from .views import SchoolclassListViews
from .views import SchoolclassDetailView
from .views import Timetable




urlpatterns = [
    path("student/", StudentListViews.as_view(), name="student_list_view"),
    path("classperiod/", ClassperiodListViews.as_view(), name="classperiod_list_view"),
    path("schoolclass/",SchoolclassListViews.as_view(),name="schoolclass_list_views"),
    path("course/", CourseListViews.as_view(), name="course_list_view"),
    path("teacher/", TeacherListViews.as_view(), name="teacher_list_view"),
    path("student/<int:id>/", StudentDetailView.as_view(), name="Student_detail_view"),
    path("course/<int:id>/", CourseDetailView.as_view(), name="Course_detail_view"),
    path("classperiod/<int:id>/", ClassperiodDetailView.as_view(), name="Classperiod_detail_view"),
    path("schoolclass/", SchoolclassDetailView.as_view(), name="schoolclass_list_views"),
    path('views/timetable/', Timetable.as_view(), name='timetable')
    ]
