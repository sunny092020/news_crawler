from rest_framework import generics
from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all().order_by("-published_date")
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["category__id"]
    filterset_fields = ["category__id"]


class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all().order_by("name")  # Order by name
    serializer_class = CategorySerializer
