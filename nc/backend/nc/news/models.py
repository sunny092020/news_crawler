from django.db import models
from django.conf import settings
import logging
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

logger = logging.getLogger(__name__)


class Article(models.Model):
    title = models.CharField(max_length=200, blank=False)
    url = models.URLField(max_length=500, unique=True, blank=False, null=False)
    author = models.CharField(max_length=100, null=True)
    published_date = models.DateTimeField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    site = models.CharField(max_length=100, blank=False)
    thumbnail = models.URLField(max_length=500, blank=True, null=True)
    summary = models.TextField(blank=False, null=False)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        print("print self.title22: ", self.title)
        return self.title

    def get_thumbnail_from_content(self):
        if self.content is None:
            return settings.DEFAULT_THUMBNAIL_URL

        # Create a BeautifulSoup object from the content
        soup = BeautifulSoup(self.content, features="html.parser")

        # Try to find all images in the content
        imgs = soup.find_all("img")
        max_size = 0
        max_url = ""
        for img in imgs:
            image_url = img.get("data-src")
            if image_url is None:
                image_url = img.get("src")

            if image_url is None:
                continue

            # If the image URL is relative, make it absolute
            if not image_url.startswith("http") and not image_url.startswith("https"):
                base_url = self.url.rsplit("/", 1)[
                    0
                ]  # remove the last part of the article URL
                image_url = urljoin(base_url, image_url)

            try:
                # Check if the image URL is reachable
                response = requests.head(image_url)
                if response.status_code == 200:
                    # Get the size of the image
                    size = int(response.headers.get("content-length", "0"))
                    if size > max_size:
                        max_size = size
                        max_url = image_url
            except requests.exceptions.RequestException as e:
                logger.error("Error while getting the image %s: %s", image_url, e)
        if max_size > 0:
            return max_url

        # If no image is found, return the default thumbnail
        return settings.DEFAULT_THUMBNAIL_URL

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.name
