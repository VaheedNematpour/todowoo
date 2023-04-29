from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'important', 'created', 'user']


class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'important', 'created']

    def create(self, validated_data):
        user_id = self.context['user_id']
        return Todo.objects.create(user_id=user_id, **validated_data)


class UpdateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'completed']
