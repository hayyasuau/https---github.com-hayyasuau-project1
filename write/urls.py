from django.urls import path
from . import views



app_name = 'write'

urlpatterns = [
    path('free/', views.free, name='free'),
    # path('join/', views.join, name='join'),
    path('join/', views.join_detail, name='join_detail'),
    path('join/comment/', views.join_comment, name='join_comment'),
    # path('join/update/<int:pk>/', views.join_update, name='join_update'),
    # path('join/delete/<int:pk>/', views.join_delete, name='join_delete'),
    path('join/join_write/', views.join, name='join_write'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<int:pk>/', views.gallery_single, name='gallery_single'),
    path('new_face/', views.new_face, name='new_face'),
    path('gallery/gallery_makeit/', views.gallery_makeit, name='gallery_makeit'),
    path('', views.board_list, name='board_list'),
    # path('borad_left/', views.borad_left, name='borad_left'),
    path('free/free_write/', views.board_free_write, name='free_write'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    # path('gallery/<int:pk>/', views.gallery_detail, name='gallery_detail'),
    path('<int:free_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:free_pk>/likes/', views.likes, name='likes'),
    path('freeboard_index/', views.freeboard_index, name='freeindex'),#자유게인덱스
    path('viewtext/<int:pk>/', views.view_text, name='free01' ),#view text, vt 게시물보기
    path('viewtext/<int:pk>/delete/', views.text_delete, name='delete' ),
    path('viewtext/<int:pk>/modify/', views.text_modify, name='modify' ),
]