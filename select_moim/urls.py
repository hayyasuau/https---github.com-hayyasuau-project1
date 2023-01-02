from django.urls import path
from . import views  




app_name = 'select_moim'

urlpatterns = [
    path('', views.select_moim, name='select_moim'),
    
    path('detail/<int:id>', views.make_detail, name='make_detail'),
    path('update/<int:id>', views.make_update, name='make_update'),
]