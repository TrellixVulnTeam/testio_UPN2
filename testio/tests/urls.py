from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('tags/', views.tags,name='tags'),
    path('tests/',views.tests,name='tests')
]
