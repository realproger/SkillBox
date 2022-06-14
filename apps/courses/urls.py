from django.urls import path 
from apps.courses.views import course_detail, course_search, enroll, panel, allcourses, listcourse


urlpatterns = [
    path('course/<int:id>', course_detail, name = "course_detail"),
    path('search/',  course_search, name="course_search"),
    path('enrollment/', enroll, name="enroll"),
    path('dashe/', panel, name="panel"),
    path('course_collection/', allcourses, name="allcourses"),
    path('courseslist/', listcourse, name="listcourse"),
]
