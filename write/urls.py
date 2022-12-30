from django.urls import path
from . import views

app_name = 'write'

urlpatterns = [
    path('free/', views.free, name='free'),
    path('join/', views.join, name='join'),
    path('join/join_write/', views.join, name='join_write'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/gallery_write/', views.gallery, name='gallery_write'),
    path('', views.board_list, name='board_list'),
    path('free/free_write/', views.board_free_write, name='free_write'),
]