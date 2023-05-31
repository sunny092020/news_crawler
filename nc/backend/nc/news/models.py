from django.db import models
from django.conf import settings
from dateutil.relativedelta import relativedelta
from botocore.exceptions import ClientError
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=500, unique=True)
    author = models.CharField(max_length=100, blank=True)
    published_date = models.DateTimeField()
    content = models.TextField()
    site = models.CharField(max_length=100)

    def __str__(self):
        return self.title

