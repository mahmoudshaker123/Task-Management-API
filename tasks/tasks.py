from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from datetime import date, timedelta
from .models import Task


@shared_task
def send_task_creation_email(task_id):
    from .models import Task  
    task = Task.objects.get(id=task_id)
    
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

@shared_task
def send_task_reminder_emails():
    # Get all tasks that are due tomorrow
    tomorrow = date.today() + timedelta(days=1)
    tasks = Task.objects.filter(due_date=tomorrow)

    for task in tasks:
        subject = "Task Reminder"
        message = f"""
        Hello {task.created_by.username},

        Just a reminder that your task '{task.title}' is due tomorrow!

        🔹 Due Date: {task.due_date}
        🔹 Priority: {task.priority}

        Please make sure to complete it on time.

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
