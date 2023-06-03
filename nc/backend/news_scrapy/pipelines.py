from asgiref.sync import sync_to_async
from nc.news.models import Article, Category
from nc.news.tasks import process_item
import logging


class NewsScrapyPipeline:
    def process_item(self, item, spider):
        logging.debug("Item: %s", item)
        process_item.delay(dict(item))
        return item

    @staticmethod
    @sync_to_async
    def save_article(item):
        internal_category_name = item["category"]
        internal_category = Category.objects.filter(name=internal_category_name).first()
        item["category"] = internal_category
        article = Article(**item)
        article.thumbnail = article.get_thumbnail_from_content()

        try:
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
        except Exception as e:
            logging.error("Error when saving article: %s", e)
            logging.error("Article: %s", article.url)
