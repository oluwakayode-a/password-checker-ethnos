# Secure Password Leak Detection System

This project is a Secure Password Leak Detection System built using Django, Celery, PostgreSQL, Redis, and Sentry. The system allows users to check if their passwords have been leaked using the HIBP (Have I Been Pwned) API. The project is designed to handle requests efficiently with background task processing, caching, and error logging.

### Project Structure

* `accounts`: Contains the user management app.
* `config`: Contains the project configuration, including settings, URLs, WSGI, and ASGI configurations.
* `main`: Contains the main app for password checking, including models, views, tasks, and migrations.
* `manage.py`: Django's command-line utility for administrative tasks.
* `requirements.txt`: Lists the project's dependencies.
* `run_celery.sh`: Script to run the Celery worker.
* `.gitignore`: Specifies files and directories to be ignored by Git.
* `README.md`: Project description and setup instructions.


### Features

Password Check API: An endpoint to check if a password has been leaked.
Asynchronous Processing: Uses Celery to process password checks in the background.
Task Status Endpoint: Allows users to poll the status of their password check tasks.
Database Storage: Stores password check results in PostgreSQL.
Caching: Uses Redis to cache password check results for 24 hours.
Error Logging: Integrates Sentry for error logging and monitoring.

### Setup Instructions

1. Clone the Repository
```bash
git clone <repository-url>
cd password-detection
```

2. Create a Virtual Environment and Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Configure PostgreSQL Database

- Ensure PostgreSQL is installed and running.
- Create a database and user for the project.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pwddetect',                      
        'USER': 'truser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
```

4. Run Migrations
```bash
python manage.py migrate
```

5. Start Redis Server
```bash
redis-server
```

6. Run Celery Worker
```bash
./run_celery.sh
```

7. Run the Django Development Server
```bash
python manage.py runserver
```

8. Access the Application

Open your browser and navigate to 
`http://127.0.0.1:8000/`.
Use the `/check-password/` endpoint to check passwords.
Use the `/task-status/<task_id>/` endpoint to check the status of password check tasks.

### Additional Information

- Sentry Integration: Ensure you have a Sentry DSN and update it in settings.py and celery.py.

- Celery Configuration: Celery is configured to use Redis as the broker and result backend.