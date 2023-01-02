from django.urls import path
from . import views  




app_name = 'select_moim'

urlpatterns = [
    path('', views.select_moim, name='select_moim'),
    # path('<int:id>', Select_DetailView.as_view()),#여기부터 시작
]