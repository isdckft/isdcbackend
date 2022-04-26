from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic import TemplateView
from django.urls import reverse

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "This is the isdcbackend site"
        context['text'] = 'Welcome'

        return context
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
