# 🚀 candidate profile backend

A modern, scalable Django backend with PostgreSQL, Redis caching, MinIO storage, JWT authentication, and more.  
Built for performance, security, and developer happiness.

LiquidGem Backend is your go-to API server for company user management, file storage, notifications,
and analytics — built with love 💎 and Python.

## ✨ Features

- 🔐 JWT Authentication & Permissions  
- 🗂 PostgreSQL database with advanced models & pagination  
- ⚡ Redis caching for blazing-fast responses  
- 🖼 MinIO/S3 storage with public & private media handling  
- 📧 Email notifications (HTML supported)  
- 📲 SMS notifications via provider API  
- 📜 Auto-generated API docs with DRF Spectacular  
- 🧪 Ready for testing and production deployment  


📁 1. Create and Activate a Virtual Environment

# In your empty project folder:

```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

📦 2. Install Django and Django REST Framework
```
pip install django djangorestframework
pip install markdown          # Markdown support for browsable API
pip install django-filter     # Filtering support
pip install drf-spectacular   # API documentation
pip install Pillow            # Required for ImageField
pip install django-storages[boto3] requests  # MinIO/S3 and HTTP requests

```


🏗️ 3. Create Django Project and App

``` 
django-admin startproject myproject .
python manage.py startapp core

```

🧩 4. Register App and REST Framework in settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'myapp',
]

5️⃣ Make and Run Migrations

```
python manage.py makemigrations
python manage.py migrate

```

6️⃣ Run the Development Server
`python manage.py runserver 8009`


# api documentation 

`pip install drf-spectacular`

INSTALLED_APPS = [
    # ALL YOUR APPS
    'drf_spectacular',
]

📚 API Documentation

`http://127.0.0.1:8009//api/docs/swagger/`

# lets save requirements to file
`pip freeze > requirements.txt`

# to install requirements
`pip install --no-cache-dir -r requirements.txt`

