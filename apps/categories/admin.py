from django.contrib import admin
from apps.categories.models import SubCategory, Category
# Register your models here.
admin.site.register(SubCategory)
admin.site.register(Category)
