from django.urls import path
from webpages import views

urlpatterns = [
    path('pagetypes/', views.pagetype_list),
    path('pagetype/<int:pk>/', views.pagetype_detail),
    path('pagetype-post/', views.pagetype_post),
    path('pagetype-put/<int:pk>/', views.pagetype_put),
    path('webpages/', views.webpage_list),
    path('webpage/<int:pk>/', views.webpage_detail),
    path('webpage-name/<str:name>/', views.webpage_name),
    path('webpage-post/', views.webpage_post),
    path('webpage-put/<int:pk>/', views.webpage_put),
]