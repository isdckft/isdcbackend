from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
from django import template
register = template.Library()

class PageType(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("webpages:pagetype_list")

class WebPage(models.Model):
    pagetype = models.ForeignKey(PageType, on_delete=models.CASCADE)
    name = models.CharField(max_length=128,unique=True)
    about = models.CharField(max_length=2048)
    url = models.URLField(max_length=254)
    official = models.BooleanField()
    date = models.DateField()

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("webpages:webpage_detail",kwargs={'pk':self.pk})