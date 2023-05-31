from django.db import models
from django.conf import settings
from dateutil.relativedelta import relativedelta
from botocore.exceptions import ClientError
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class Article(models.Model):
    title = models.CharField(max_length=200, blank=False)
    url = models.URLField(max_length=500, unique=True, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False)
    published_date = models.DateTimeField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    site = models.CharField(max_length=100, blank=False)

    def __str__(self):
        print("print self.title22: ", self.title)
        return self.title
