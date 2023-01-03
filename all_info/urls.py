from django.urls import path
from . import views

app_name = 'all_info'

urlpatterns = [
    path('<str:id>', views.detail, name='detail'),
    path('', views.profile_view, name='profile_view'),
    path('update/<str:id>/', views.update, name='update'),
    # path('update', views.profile_update_view, name='profile_update_view'),

]