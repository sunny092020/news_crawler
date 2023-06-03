from celery import shared_task
from django.core.exceptions import ValidationError
from nc.news.models import Article
from bulk_sync import bulk_sync

bulk_queue = []

@shared_task
def process_item(item):
    bulk_queue.append(Article(**item))
    
    # If bulk_queue has 100 items, save them in a bulk operation
    if len(bulk_queue) >= 100:
        save_items()

def save_items():
    for item in bulk_queue:
        print(item)

    # Empty the queue
    del bulk_queue[:]
