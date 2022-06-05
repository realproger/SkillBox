from tabnanny import verbose
from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
         return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class Partners(models.Model):
    name = models.CharField(max_length=255)
    partners_image = models.ImageField(upload_to = "partners_image/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Партнёр"
        verbose_name_plural = "Партнёры"

class AboutFeatures(models.Model):
    course_features = models.CharField(max_length=255)

    def __str__(self):
        return self.course_features

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"
    
class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    about_features = models.ManyToManyField(AboutFeatures, verbose_name="Характеристики", related_name="about_feature")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
