from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('remove_task/<int:task_id>', views.remove_task, name='remove_task'),

]
