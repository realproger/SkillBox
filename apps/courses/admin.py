from django.contrib import admin
from apps.courses.models import CourseFeatures, AcquiredKnowledge, Course, CourseComment, SubCourses
# Register your models here.
admin.site.register(CourseFeatures)
admin.site.register(AcquiredKnowledge)
admin.site.register(Course)
admin.site.register(CourseComment)
admin.site.register(SubCourses)
