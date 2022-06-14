from multiprocessing import context
from django.shortcuts import render
from apps.news.models import News
from apps.settings.models import Setting
from apps.categories.models import Category
# Create your views here.
def newsreport(request):
    home = Setting.objects.latest('id')
    categories = Category.objects.all()
    news = News.objects.all().order_by('-id')
    context = {
        'home' : home, 
        'categories' : categories,
        'news' : news,
    }

    return render(request, 'blogs.html', context)

def reportdetail(request, id):
    news = News.objects.get(id = id)
    home = Setting.objects.latest('id')
    categories = Category.objects.all()
    new = News.objects.all()
    random_news = News.objects.all().order_by('-id')[:5]

    context = {
        'news' : news,
        'home' : home, 
        'categories' : categories, 
        'new' : new,
        'random_news' : random_news,
    }

    return render(request, 'blog-detail.html', context)