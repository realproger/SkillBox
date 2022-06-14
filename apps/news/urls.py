from django.urls import path
from apps.news.views import newsreport, reportdetail

urlpatterns = [
    path('newsreport/', newsreport, name="newsreport" ),
    path('newsdetail/<int:id>', reportdetail, name="reportdetail"),
]