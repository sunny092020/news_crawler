import pytest

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mtfu.settings")
django.setup()

from rest_framework.test import APIClient

from nc.news.models import Article, Category
from nc.tests.utils import get_content_from_response


@pytest.fixture
def categories():
    categorie_names = [
        "Thời sự",
        "Thế giới",
        "Kinh doanh",
        "Giải trí",
        "Thể thao",
        "Pháp luật",
        "Giáo dục",
        "Sức khỏe",
        "Đời sống",
        "Du lịch",
        "Khoa học",
        "Khác",
    ]

    for categorie_name in categorie_names:
        Category.objects.update_or_create(name=categorie_name)

    return Category.objects.all()


@pytest.fixture
def articles(categories):
    for category in categories:
        for i in range(1, 3):
            Article.objects.update_or_create(
                title=f"Article {i}",
                url=f"https://www.{category.name.replace(' ', '').lower()}.com/article-{i}",
                author="Author",
                published_date="2020-01-01T00:00:00Z",
                content="Content",
                site="Site",
                thumbnail="Thumbnail",
                summary="Summary",
                category=category,
            )

    return Article.objects.all()


# test GET /api/v1/articles/<ID>
def test_get_article(articles):
    client = APIClient()
    article = articles[0]
    response = client.get(f"/api/v1/articles/{article.id}/")
    assert response.status_code == 200
    assert get_content_from_response(response)["title"] == article.title


# test GET /api/v1/articles?category__id=<CATEGORY_ID>
def test_get_articles_by_category(articles):
    client = APIClient()
    category = articles[0].category
    response = client.get(f"/api/v1/articles?category__id={category.id}")
    assert response.status_code == 200
    content = get_content_from_response(response)
    assert len(content["results"]) == 2


# test GET /api/v1/categories
def test_get_categories(categories):
    client = APIClient()
    response = client.get("/api/v1/categories/")
    assert response.status_code == 200
    content = get_content_from_response(response)
    assert len(content) == 12
