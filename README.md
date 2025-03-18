# Task Management API

## Project Description
This is a Task Management API that allows users to create, manage, and track tasks. Users can register, log in, create tasks, assign tasks to other users, and filter tasks based on status, priority, or due date.

## Features

### 1. User Authentication and Authorization
- Users can register and log in using email and password.
- Uses JWT (JSON Web Tokens) authentication for secure API access.
- Only authenticated users can create, update, or delete tasks.

### 2. Task Management
- Users can create tasks with the following fields:
  - Title
  - Description
  - Due date
  - Priority (Low, Medium, High)
  - Status (To Do, In Progress, Done)
- Users can assign tasks to other users.
- Users can update or delete their own tasks.

### 3. Task Filtering and Sorting
- Users can filter tasks by:
  - Status
  - Priority
  - Due date
- Users can sort tasks by:
  - Due date (ascending/descending)
  - Priority (ascending/descending)

### 4. User Profile
- Users can view their profile, which includes:
  - Name
  - Email
  - List of tasks assigned to them
  - List of tasks created by them

### 5. Bonus Features (Optional)
- Pagination for task lists.
- Email notifications for task assignments or due date reminders.
- Search functionality for tasks by title or description.

## Technology Stack
- **Backend Framework:** Django & Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Tokens)
- **Task Queue (Optional):** Celery with Redis
- **API Documentation:**  Swagger

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/mahmoudshaker123/Task-Management-API.git
cd Task-Management-API
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and set up the following environment variables:
```ini
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgresql://postgres:postgres@db:5432/tasks
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

## Running with Docker

### 1. Build and Run Docker Containers
```bash
docker-compose up --build
```

### 2. Run Migrations inside the Container
```bash
docker-compose exec djangoserver python manage.py migrate
```

### 3. Create a Superuser
```bash
docker-compose exec djangoserver python manage.py createsuperuser
```

### 4. Access the Application
- API Base URL: `http://localhost:8000/api/`


## Author
Developed by [Mahmoud shaker].

