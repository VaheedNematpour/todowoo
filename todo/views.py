from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from . import serializers


class TodoViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        return Todo.objects.filter(user_id=self.request.user.id, completed__isnull=True)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateTodoSerializer
        elif self.request.method == 'PUT':
            return serializers.UpdateTodoSerializer
        return serializers.TodoSerializer

    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}


class CompletedTodoViewSet(ModelViewSet):
    http_method_names = ['get']

    def get_queryset(self):
        return Todo.objects.filter(user_id=self.request.user.id, completed__isnull=False)

    serializer_class = serializers.TodoSerializer
