from django.urls import path
from . import views

app_name = 'write'

urlpatterns = [
    path('free/', views.free, name='free'),
    path('join/', views.join, name='join'),
    path('gallery/', views.gallery, name='gallery'),
    path('', views.board_list, name='board_list'),
    path('free_write/', views.board_free_write, name='free_write'),
]