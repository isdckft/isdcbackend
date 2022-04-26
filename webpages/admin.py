from django.contrib import admin

# Register your models here.
from .models import PageType
admin.site.register(PageType)

from .models import WebPage
admin.site.register(WebPage)

