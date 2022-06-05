from django.shortcuts import render
from apps.settings.models import Setting
from apps.courses.models import Course, CourseComment
from apps.categories.models import Category
# Create your views here.
def research_category(request):
    home = Setting.objects.latest('id')
    courses = Course.objects.all()
    categories = Category.objects.all()

    context = {
        'home' : home,
        'courses' : courses,
        'categories' : categories,
    }
    return render(request, 'courses/explore-category.html', context)

def sort_course(request, id):
    home = Setting.objects.latest('id')
    courses = Course.objects.all()
    categories = Category.objects.get(id = id)

    context = {
        'home' : home,
        'courses' : courses,
        'categories' : categories,
    }
    return render(request, 'courses/sortcourses.html', context)