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
        article.save()
