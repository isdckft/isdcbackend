from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import PageType
from .serializers import PageTypeSerializer
from .models import WebPage
from .forms import WebPageForm, PageTypeForm
from .serializers import WebPageSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView,DetailView,CreateView,DeleteView,
                                UpdateView)
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin


@csrf_exempt
@api_view(['GET'])
@permission_classes([permissions.AllowAny,]) # everybody cab access it
def pagetype_list(request):
    """
    PageType List, it gives back the list of the types
    """

    pagetypes = PageType.objects.all()
    serializer = PageTypeSerializer(pagetypes, many=True)
    return JsonResponse(serializer.data, safe=False)


# Get One Page Type
@csrf_exempt
@api_view(['GET'])
@permission_classes([permissions.AllowAny,]) # everybody can access it
def pagetype_detail(request, pk):
    pagetype = PageType()
    try:
        pagetype = PageType.objects.get(pk=pk)
    except pagetype.DoesNotExist:
        return HttpResponse(status=404) # Not Found

    serializer = PageTypeSerializer(pagetype)
    return JsonResponse(serializer.data)

# Post a new page type
@csrf_exempt
@api_view(['POST'])
def pagetype_post(request):

    data = JSONParser().parse(request)
    serializer = PageTypeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400) # Bad request

# Update or delete a Page type
@csrf_exempt
@api_view(['PUT','DELETE'])
def pagetype_put(request, pk):
    pagetype = PageType()
    try:
        pagetype = PageType.objects.get(pk=pk)
    except pagetype.DoesNotExist:
        return HttpResponse(status=404) # Not Found
    
    # Update one page type
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PageTypeSerializer(pagetype, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    # detete one page type
    elif request.method == 'DELETE':
        pagetype.delete()
        return HttpResponse(status=204)

# Get all web pages
@csrf_exempt
@api_view(['GET'])
@permission_classes([permissions.AllowAny,]) # everybody can access it
def webpage_list(request):

    webpages = WebPage.objects.all()
    serializer = WebPageSerializer(webpages, many=True)
    return JsonResponse(serializer.data, safe=False)


# Get a web page by ID
@csrf_exempt
@api_view(['GET'])
@permission_classes([permissions.AllowAny,]) # everybody can access it
def webpage_detail(request, pk):
    webpage = WebPage()
    try:
        webpage = WebPage.objects.get(pk=pk)
    except webpage.DoesNotExist:
        return HttpResponse(status=404)

    serializer = WebPageSerializer(webpage)
    return JsonResponse(serializer.data)

# Get a web page by Name
@csrf_exempt
@api_view(['GET'])
@permission_classes([permissions.AllowAny,]) # everybody can access it
def webpage_name(request, name):
    webpage = WebPage()
    try:
        webpage = WebPage.objects.get(name=name)
    except webpage.DoesNotExist:
        return HttpResponse(status=404)
   
    serializer = WebPageSerializer(webpage)
    return JsonResponse(serializer.data)


# Post a new webpage
@csrf_exempt
@api_view(['POST'])
def webpage_post(request):

    data = JSONParser().parse(request)
    serializer = WebPageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

# Update or delete a webpage
@csrf_exempt
@api_view(['PUT','DELETE'])
def webpage_put(request, pk):
    webpage = WebPage()
    try:
        webpage = WebPage.objects.get(pk=pk)
    except webpage.DoesNotExist:
        return HttpResponse(status=404)

    # update one web page    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WebPageSerializer(webpage, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    # delete one web page
    elif request.method == 'DELETE':
        webpage.delete()
        return HttpResponse(status=204)
    
"""
These are normal views , render to the Django front-end
"""

class WebpageListView(ListView):
    template_name = 'webpages/webpages.html'
    context_object_name = 'webpages'
    model = WebPage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = 'These are my favorite cool webpages'
        return context

    def get_queryset(self):
        return WebPage.objects.order_by('name')

class PageTypeListView(ListView):
    template_name = 'webpages/pagetypes.html'
    context_object_name = 'pagetypes'
    model = PageType

class WebPageDetailView(DetailView):
    context_object_name = 'webpage_details'
    model = WebPage
    template_name = 'webpages/webpage_detail.html'

class PageTypeCreateView(LoginRequiredMixin,CreateView):
    template_name = 'webpages/pagetype_form.html'
    #fields = ("name",)
    
    login_url = '/accounts/login/'
    form_class = PageTypeForm
    model = PageType


class PageTypeUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'webpages/pagetype_form.html'
    fields = ("name",)
    login_url = '/accounts/login/'
    model = PageType

class WebPageDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'webpages/webpage_delete.html'
    model = WebPage
    login_url = '/accounts/login/'
    success_url = reverse_lazy("webpages:webpage_list")

class PageTypeDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'webpages/pagetype_delete.html'
    model = PageType
    login_url = '/accounts/login/'
    success_url = reverse_lazy("webpages:pagetype_list")

class WebPageCreateView(LoginRequiredMixin,CreateView): 
    template_name = 'webpages/webpage_form.html'
    model = WebPage

    login_url = '/accounts/login/'
    success_url = reverse_lazy("webpages:webpage_list")
    form_class = WebPageForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form) 

class WebPageUpdateView(LoginRequiredMixin,UpdateView): 
    template_name = 'webpages/webpage_form.html'
    model = WebPage

    login_url = '/accounts/login/'
    success_url = reverse_lazy("webpages:webpage_list")
    form_class = WebPageForm

    def form_valid(self, form):
        self.object = form.save(commit=True)
        return super().form_valid(form) 
