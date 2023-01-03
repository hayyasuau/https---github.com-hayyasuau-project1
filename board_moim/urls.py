
from django.urls import path
from . import views



app_name = 'board_moim'

urlpatterns = [
    path('', views.board_moim, name='board_moim'),
    path('list/', views.list_moim, name='list_moim'),
    # path('list/<str:search>', views.search, name='search'),
]