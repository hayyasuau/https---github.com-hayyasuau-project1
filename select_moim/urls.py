from django.urls import path
from . import views  




app_name = 'select_moim'

urlpatterns = [
    path('', views.select_moim, name='select_moim'),
]