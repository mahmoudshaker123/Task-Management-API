from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly
from .tasks import send_task_creation_email


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated , IsOwnerOrReadOnly ]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['status', 'priority', 'due_date']
    ordering_fields = ['due_date', 'priority']
    search_fields = ['title', 'description']
    
    def perform_create(self, serializer):
            task = serializer.save(created_by=self.request.user)  
            send_task_creation_email.delay(task.id)
           

