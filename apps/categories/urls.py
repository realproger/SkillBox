from django.urls import path 
from apps.categories.views import research_category, sort_course


urlpatterns = [
    path('category_research/', research_category, name="research" ),
    path('courses/<int:id>', sort_course, name="sort_course"),
]
