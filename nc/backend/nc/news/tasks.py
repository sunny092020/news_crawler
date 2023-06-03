from celery import shared_task
from nc.news.models import Article, Category


@shared_task
def process_item(item):
    internal_category_name = item["category"]
    internal_category = Category.objects.filter(name=internal_category_name).first()
    item["category"] = internal_category
    article = Article(**item)
    article.thumbnail = article.get_thumbnail_from_content()

    # update_or_create() will update the article if it already exists
    # based on the unique URL field
    Article.objects.update_or_create(
        url=article.url,
        defaults={
            "title": article.title,
            "author": article.author,
            "published_date": article.published_date,
            "content": article.content,
            "site": article.site,
            "thumbnail": article.thumbnail,
            "summary": article.summary,
            "category": article.category,
        },
    )
