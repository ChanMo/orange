from django.db import models
import bleach
from bs4 import BeautifulSoup
from django.utils.html import strip_tags
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextUploadingField(null=True, blank=True)
    link = models.URLField(blank=True, null=True)
    template = models.CharField(max_length=200, default='default')
    is_show = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_description(self, count=200):
        """Get description, default 200 words"""
        #return strip_tags(self.content)[0:200]
        return bleach.clean(strip_tags(self.content), strip=True)[0:count]

    def get_cover(self):
        """Get page's cover, use the first image of content"""
        tree = BeautifulSoup(self.content, "html5lib")
        cover = tree.find('img')
        if cover:
            return cover['src']
        else:
            return None

    #def get_link(self):
    #    """Get page' link"""
    #    if self.link:
    #        return self.link
    #    else:
    #        return 'http://%s/%s' % (settings.ALLOWED_HOSTS[0], self.slug)
