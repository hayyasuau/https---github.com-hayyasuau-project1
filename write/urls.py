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
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:free_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:free_pk>/likes/', views.likes, name='likes'),
]