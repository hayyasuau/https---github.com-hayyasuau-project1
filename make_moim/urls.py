from django.urls import path
from . import views



app_name = 'make_moim'

urlpatterns = [
    path('', views.make_moim, name='make_moim'),
]