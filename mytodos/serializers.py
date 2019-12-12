from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','title','description','done','due_date')
        model = ToDo