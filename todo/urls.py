from django.urls import path, include
from . import views

app_name = 'todo'

urlpatterns = [
  path('', views.TodoListCreate.as_view(), name='todo_list_create'),
  path('<pk>/', views.TodoRetrieveUpdateDelete.as_view(), name='todo_retrieve_update_delete'),
]