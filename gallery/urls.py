from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('get-video/', views.get_video, name = 'get-video'),
]