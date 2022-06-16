from distutils.command.upload import upload
from django.db import models
from apps.categories.models import Category
from apps.courses.models import Course
from apps.settings.models import About
from apps.users.models import User
# Create your models here.

class News(models.Model):
    title = models.TextField()
    reporter = models.CharField(max_length=255)
    news_image = models.ImageField(upload_to = "imagenews/")
    description = models.TextField()
    main_text = models.TextField()
    news_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categorynews")
    news_quotes = models.TextField()
    author_quote = models.CharField(max_length=255)
    posted = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    



    