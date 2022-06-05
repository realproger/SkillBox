from django.db import models
from apps.categories.models import SubCategory, Category
from apps.users.models import User

# Create your models here.
class CourseFeatures(models.Model):
    course_features = models.CharField(max_length=255)

    def __str__(self):
        return self.course_features

    class Meta:
        verbose_name = "Характеристика курсов"
        verbose_name_plural = "Характеристики курсов"

class AcquiredKnowledge(models.Model):
    acquirements = models.TextField()

    def __str__(self):
        return self.acquirements

    class Meta:
        verbose_name = "Приобретение знания"
        verbose_name_plural = "Приобретения знаний"

class SubCourses(models.Model):
    subcourse = models.CharField(max_length=255)

    def __str__(self):
        return self.subcourse
    
    class Meta:
        verbose_name = "Подкурс"
        verbose_name_plural = "Подкурсы"


class Course(models.Model):
    title = models.CharField(max_length=255)
    course_image = models.ImageField(upload_to = "team_image/")
    spendtime = models.CharField(max_length=255)
    students = models.CharField(max_length=255)
    about_course = models.TextField()
    raiting = models.IntegerField()
    price = models.IntegerField()
    price_info = models.CharField(max_length=255)
    course_features = models.ManyToManyField(CourseFeatures, verbose_name="Характеристики курсов", related_name="course_feature")
    acquirements = models.ManyToManyField(AcquiredKnowledge, verbose_name="Приобретение знания", related_name="acquirement")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="curscategory")
    description = models.TextField()
    content = models.ManyToManyField(SubCourses, verbose_name="Подкурсы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

class CourseComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_course")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_comment" )
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message 

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"


