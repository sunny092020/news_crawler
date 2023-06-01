from .views import ArticleList, ArticleDetail
from django.urls import path

urlpatterns = [
    path("articles", ArticleList.as_view(), name="news.articles"),
    path("articles/<int:pk>/", ArticleDetail.as_view(), name="article_detail"),
]
