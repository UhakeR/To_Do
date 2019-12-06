from django.urls import path
from .views import TodoListView, TodoCreateView, TodoDetailView, TodoDeleteView, TodoUpdateView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo'),
    path('new/', TodoCreateView.as_view(), name='new'),
    path('<int:pk>/', TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit/', TodoUpdateView.as_view(), name='edit'),
]