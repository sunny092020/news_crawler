from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-published_date')
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["category__id"]
    filterset_fields = ["category__id"]


class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
