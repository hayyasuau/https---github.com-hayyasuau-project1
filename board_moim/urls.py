
from django.urls import path
from . import views



app_name = 'board_moim'

urlpatterns = [
    path('', views.board_moim, name='board_moim'),
]