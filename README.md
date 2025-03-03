# Note Managing App

## Overview ##

The Note Managing App is a full-stack application built using Next.js for the frontend and Django (Django REST Framework) for the backend. This guide provides step-by-step instructions to set up and run the project locally.

## Tech Stack

Frontend: Next.js, React, Tailwind CSS

Backend: Django, Django REST Framework

Database: SQLite

API Communication: REST API

Prerequisites

Before starting, ensure you have the following installed:

Node.js (>= 16)

Python (>= 3.9)

pip and virtualenv

Postman (optional for API testing)

## Installation Guide

1️⃣ Backend Setup (Django API)

**1. Clone the Repository**

`git clone https://github.com/Imanolasolo/note-manager-backend.git

`cd note-manager`

**2. Create a Virtual Environment**
```
python -m venv venv
source venv/bin/activate   # On MacOS/Linux
venv\Scripts\activate     # On Windows
```

**3. Install Dependencies**
```python
pip install -r requirements.
```

**4. Run Database Migrations**
```
python manage.py migrate
```
**5. Create a Superuser (Admin Access)**

```
python manage.py createsuperuser
```

Follow the prompts to set up an admin account.

**6. Start the Backend Server**
```
python manage.py runserver
```

The backend will run on http://127.0.0.1:8000/

2️⃣ Frontend Setup (Next.js)

```
git clone https://github.com/Imanolasolo/note_manager_frontend.git
```

1. Navigate to newly created Folder

2. Install Dependencies
```
npm install
```
3. Start the Development Server
```
npm run dev
```
The frontend will be available at http://localhost:3000/

API Endpoints

🔹 User Authentication

Register: **POST /api/api/register/**

Login: **POST /api/api/login/**

🔹 Notes Management

Create Note: **POST /api/notes/**

List Notes: **GET /api/notes/**

Update Note: **PUT /api/notes/{id}/**

Delete Note: **DELETE /api/notes/{id}/**

Testing the API

You can use Postman or cURL to test the endpoints.

Example request to register a user:

curl -X POST http://127.0.0.1:8000/api/api/register/ \  
    -H "Content-Type: application/json" \  
    -d '{"username": "testuser", "password": "password123"}'

Environment Variables

Create a .env.local file in the frontend directory and add:

NEXT_PUBLIC_API_URL=http://127.0.0.1:8000/api/

## Deployment Guide ##

For production deployment:

Use Gunicorn & Nginx for Django backend.

Use Vercel or Netlify for the Next.js frontend.

Contribution Guide

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Make changes and commit (git commit -m "Added new feature").

Push the branch (git push origin feature-branch).

Open a Pull Request.

## License

This project is licensed under the MIT License.

Author

# Imanol Asolo  🚀



