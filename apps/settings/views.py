from pkgutil import ImpImporter
from django.shortcuts import render
from apps.settings.models import Setting
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



    