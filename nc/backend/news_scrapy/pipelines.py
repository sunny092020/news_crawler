# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
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
