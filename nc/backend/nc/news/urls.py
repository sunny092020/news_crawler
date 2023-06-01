from .views import ArticleList
from django.urls import path

urlpatterns = [
    path("articles", ArticleList.as_view(), name="news.articles"),
]
