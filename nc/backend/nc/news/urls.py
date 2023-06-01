from .views import ArticleList, ArticleDetail, CategoryList
from django.urls import path

urlpatterns = [
    path("articles", ArticleList.as_view(), name="news.articles"),
    path("articles/<int:pk>/", ArticleDetail.as_view(), name="article_detail"),
    path("categories/", CategoryList.as_view(), name="categories"),
]
