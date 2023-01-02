from django.urls import path
from . import views



app_name = 'make_moim'

urlpatterns = [
    path('', views.Make_Moim.as_view()),
]