from django.urls import path
from home import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
]
