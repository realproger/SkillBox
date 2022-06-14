from pkgutil import ImpImporter
from django.shortcuts import render
from apps.settings.models import Setting, Partners, AboutFeatures, About
from apps.courses.models import Course, CourseComment
from apps.categories.models import Category
from apps.users.models import User
from apps.news.models import News
# Create your views here.

def index(request):
    home = Setting.objects.latest('id')
    courses = Course.objects.all().order_by('-id')[:6]
    categories = Category.objects.all()
    comments = CourseComment.objects.all()
    users = User.objects.all()
    news = News.objects.all().order_by('-id')

    context = {
        'home' : home,
        'courses' : courses,
        'categories' : categories,
        'comments' : comments,
        'users' : users,
        'news': news,
    }
    return render(request, 'home-3.html', context)


def about(request):
    home = Setting.objects.latest('-id')
    about = About.objects.latest('id')
    partners = Partners.objects.all().order_by('-id')
    comments = CourseComment.objects.all()
    users = User.objects.all()

    context = {
        'home' : home,
        'about' : about, 
        'partners' : partners,
        'comments' : comments,
        'users' : users,
    }

    return render(request, 'about.html', context)
