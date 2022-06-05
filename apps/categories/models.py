from django.db import models


# Create your models here.
class SubCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Субкатегория"
        verbose_name_plural = "Субкатегории"

class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'main_image', blank = True, null = True)
    description = models.TextField()
    quotes = models.TextField()
    subcategory = models.ManyToManyField(SubCategory, verbose_name='Субкатегории', related_name='sub_category')
  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории "




