from rest_framework import serializers
from webpages.models import WebPage,PageType

class PageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageType
        fields = ('id','name')

class WebPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebPage
        fields = ('id','pagetype','name','about','url','official','date')

