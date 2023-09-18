from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task

# Create your views here.
# Each page on our site is generated using an object defined below
# These are referenced in ./templates html files


class TaskList(ListView):
    model = Task # this model comes from models.py
    context_object_name = 'tasks' # this allows us to reference TaskList objects as 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__' # We display all columns and rows in our database Task table
    success_url = reverse_lazy('tasks') # When a user submits the form we redirect to our "home" page


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm # This form is imported
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
