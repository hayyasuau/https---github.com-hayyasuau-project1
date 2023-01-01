from django.urls import path
from . import views



app_name = 'write'

urlpatterns = [
    path('free/', views.free, name='free'),
    path('join/', views.join, name='join'),
    path('join/join_write/', views.join, name='join_write'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<int:pk>', views.gallery_single, name='gallery_single'),
    path('new_face/', views.new_face, name='new_face'),
    path('gallery/gallery_make/', views.gallery_make, name='gallery_make'),
    path('', views.board_list, name='board_list'),
    # path('borad_left/', views.borad_left, name='borad_left'),
    path('free/free_write/', views.board_free_write, name='free_write'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    # path('gallery/<int:pk>/', views.gallery_detail, name='gallery_detail'),
    path('<int:free_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:free_pk>/likes/', views.likes, name='likes'),
]