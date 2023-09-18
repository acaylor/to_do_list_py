from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, RegisterPage

# This is the routes for our web server to serve pages
# Pages need a corresponding html template in ./templates
urlpatterns = [
    path('', TaskList.as_view(), name='tasks'), # This is effectively the home page
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('register/', RegisterPage.as_view(), name='register')
]
