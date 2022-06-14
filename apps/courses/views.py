from django.shortcuts import render
from apps.settings.models import Setting
from apps.courses.models import Course, CourseComment
from apps.categories.models import Category
from django.db.models import Q
# Create your views here.

def course_detail(request, id):
    course = Course.objects.get(id = id)
    courses = Course.objects.all()
    random_courses = Course.objects.all().order_by('?')[:5]
    home = Setting.objects.latest('id')
    categories = Category.objects.all()

    if 'comment' in request.POST:
        id = request.POST.get('post_id')
        message = request.POST.get('comment_message')
        comment = CourseComment.objects.create(message=message, course=course, user=request.user)

    context = {
        'course' : course,
        'courses' : courses,
        'random_courses' : random_courses,
        'home' : home,
        'categories' : categories,
    }
    return render(request, 'courses/detail.html', context)


def course_search(request):
    courses = Course.objects.all()
    qury_obj = request.GET.get('key')
    home = Setting.objects.latest('id')
    if qury_obj:
        courses = Course.objects.filter(Q(title__icontains = qury_obj))
    context = {
        'home' : home, 
        'courses' : courses,
    }
    return render(request, 'courses/search.html', context)



def enroll(request):
    home = Setting.objects.latest('id')
    courses = Course.objects.all()
    categories = Category.objects.all()

    context = {
        'home' : home,
        'courses' : courses,
        'categories' : categories,
    }
    return render(request, 'enroll-student.html', context)

def panel(request):
    home = Setting.objects.all()
    courses = Course.objects.all()
    categories = Category.objects.all()

    context = {
        'home' : home,
        'courses' : courses,
        'categories' : categories,
    }
    return render(request, 'dashboard.html', context)


def allcourses(request):
    home = Setting.objects.latest('id')
    courses = Course.objects.all()
    categories = Category.objects.all()

    context = {
        'home' : home,
        'courses' : courses,
        'categories' : categories,
    }
    return render(request, 'courses/grid-layout-full.html', context)


def listcourse(request):
    home = Setting.objects.all()
    courses = Course.objects.all()
    categories = Category.objects.all()

    context = {
        'home' : home,
        'courses' : courses,
        'categories' : categories,
    }
    return render(request, 'courses/list-layout-with-full.html', context)