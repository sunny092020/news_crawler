from nc.news.tasks import process_item


class NewsScrapyPipeline:
    def process_item(self, item, spider):
        process_item.delay(dict(item))
        return item
