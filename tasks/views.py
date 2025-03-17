from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly
from django.core.mail import send_mail
from django.conf import settings


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
            
            subject = "Task Created Successfully"
            message = f"""
            Hello {task.created_by.username},

            Your task '{task.title}' has been created successfully.

            🔹 Due Date: {task.due_date}
            🔹 Priority: {task.priority}

            Please check your task list for more details.

            Best Regards,
            Task Management System
            """
            recipient_email = task.created_by.email

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient_email],
                fail_silently=False,
            )