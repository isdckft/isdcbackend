from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, permission_required

# SET THE NAMESPACE!
app_name = 'webpages'

urlpatterns = [
    path('webpages/', views.WebpageListView.as_view(),name='webpage_list'),
    path('webpage-detail/<int:pk>/', views.WebPageDetailView.as_view(),name='webpage_detail'),
    path('webpage-delete/<int:pk>/', views.WebPageDeleteView.as_view(),name='webpage_delete'),
    path('webpage/', views.WebPageCreateView.as_view(), name='webpage_form'),
    path('webpage/<int:pk>/', views.WebPageUpdateView.as_view(),name='webpage_update'),
    path('pagetypes/', views.PageTypeListView.as_view(),name='pagetype_list'),
    path('pagetype/',views.PageTypeCreateView.as_view(), name='pagetype_form'),
    path('pagetype/<int:pk>/', views.PageTypeUpdateView.as_view(),name='pagetype_update'),
    path('pagetype-delete/<int:pk>/', views.PageTypeDeleteView.as_view(),name='pagetype_delete'),
]

