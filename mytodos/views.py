from rest_framework import generics
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import ToDo
from django.urls import reverse_lazy
from .serializers import ToDoSerializer
class TodoListView(ListView):
    model = ToDo
    template_name = 'todo.html'

class TodoCreateView(CreateView):
    model = ToDo
    fields = ('title', 'description', 'due_date')
    template_name = 'todo_create.html'

class TodoDetailView(DetailView):
    model = ToDo
    template_name = 'todo_detail.html'

class TodoDeleteView(DeleteView):
    model=ToDo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todo')

class TodoUpdateView(UpdateView):
    model=ToDo
    fields = ('title', 'description', 'done')
    template_name = 'todo_edit.html'

class TodoList(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class TodoDetail(generics.RetrieveDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer