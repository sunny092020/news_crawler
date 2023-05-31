from asgiref.sync import sync_to_async
from itemadapter import ItemAdapter
from nc.news.models import Article


class NewsScrapyPipeline:
    async def process_item(self, item, spider):
        article = Article(**item)
        await self.save_article(article)
        print("Saved article: ", article)
        return item

    @staticmethod
    @sync_to_async
    def save_article(article):
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
            },
        )
