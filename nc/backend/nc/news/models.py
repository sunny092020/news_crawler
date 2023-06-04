from django.db import models
from django.conf import settings
import logging
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

logger = logging.getLogger(__name__)


class Article(models.Model):
    title = models.TextField(blank=False, null=False)
    url = models.TextField(unique=True, blank=False, null=False)
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

        thumbnail_url = self.get_largest_image_url(imgs)
        if thumbnail_url:
            return thumbnail_url

        # If no image is found, return the default thumbnail
        return settings.DEFAULT_THUMBNAIL_URL

    def get_largest_image_url(self, imgs):
        max_size = 0
        max_url = ""
        for img in imgs:
            image_url = self.process_image_url(img)
            if image_url:
                size, url = self.check_image_url(image_url)
                if size > max_size:
                    max_size = size
                    max_url = url
        if max_size > 0:
            return max_url

    def process_image_url(self, img):
        image_url = img.get("data-src")
        if image_url is None:
            image_url = img.get("src")
        if image_url is None:
            return None

        # If the image URL is relative, make it absolute
        if not image_url.startswith("http"):
            base_url = self.url.rsplit("/", 1)[0]  # remove the last part of the article URL
            image_url = urljoin(base_url, image_url)

        return image_url

    def check_image_url(self, image_url):
        try:
            # Check if the image URL is reachable
            response = requests.head(image_url)
            if response.status_code == 200:
                # Get the size of the image
                size = int(response.headers.get("content-length", "0"))
                return size, image_url
        except requests.exceptions.RequestException as e:
            logger.error("Error while getting the image %s: %s", image_url, e)
        return 0, ""


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.name
