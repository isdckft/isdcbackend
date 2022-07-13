from django.urls import path
from . import views

app_name = 'ml'
urlpatterns = [
    path('iris/', views.iris, name='iris'),
    path('datapreproc/', views.dataPreProc, name='datapreproc'),

]