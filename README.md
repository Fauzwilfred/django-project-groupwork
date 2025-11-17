# Django Course Management Application

## Project Overview
This is a simple Django application for managing courses. It demonstrates basic Django concepts including models, views, URLs, and the admin interface.

---

## File Structure & Explanations

### **Project Root: `student_app/`**

#### **`manage.py`**
- **Purpose:** Command-line utility for managing Django projects
- **What it does:** Allows you to run commands like `python manage.py runserver`, `python manage.py migrate`, `python manage.py createsuperuser`, etc.
- **In simple terms:** It's the control center for your Django project - you use it to start the server, create databases, and manage your application.

---

### **Project Configuration: `student_app/student_app/`**

#### **`__init__.py`**
- **Purpose:** Makes the `student_app` directory a Python package
- **What it does:** Empty file that tells Python to treat this folder as a package
- **In simple terms:** It's a marker file that Python needs to recognize this folder as containing Python code

#### **`settings.py`**
- **Purpose:** Central configuration file for the entire Django project
- **What it does:** Contains settings like:
  - Database configuration (SQLite in this case)
  - Installed apps (admin, auth, sessions, and our `courses` app)
  - Security settings (SECRET_KEY, ALLOWED_HOSTS)
  - Templates and static files configuration
- **In simple terms:** This is where you configure everything about how Django behaves - think of it as the project's instruction manual

#### **`urls.py`**
- **Purpose:** Maps URL routes to views (pages/functions)
- **What it does:** Defines which URLs users can visit and which view function handles each URL:
  - `/` → home view
  - `/courses/` → course list view
  - `/courses/<id>/` → course detail view
  - `/admin/` → Django admin interface
- **In simple terms:** It's like a phone switchboard - when someone visits a URL, it routes them to the correct page handler

#### **`wsgi.py`**
- **Purpose:** Web Server Gateway Interface configuration
- **What it does:** Configures how the Django application communicates with web servers (for production deployment)
- **In simple terms:** It's the interface that allows web servers to run your Django app

#### **`asgi.py`**
- **Purpose:** Asynchronous Server Gateway Interface configuration
- **What it does:** Similar to WSGI but for asynchronous requests and WebSocket support
- **In simple terms:** It's for handling real-time features like chat or live updates

---

### **App: `student_app/courses/`**

#### **`models.py`**
- **Purpose:** Defines the database structure
- **What it does:** Contains the `Course` model with fields:
  - `name` - Course title (max 100 characters)
  - `description` - Detailed course description
  - `instructor` - Name of the instructor
  - `credits` - Number of credits (default 3)
  - `created_at` - Timestamp when the course was created
- **In simple terms:** This defines what data gets stored in the database and what fields each course record has

#### **`views.py`**
- **Purpose:** Contains the logic that handles user requests
- **What it does:** Defines three functions:
  - `home()` - Returns a welcome message
  - `course_list()` - Returns all courses as JSON
  - `course_detail()` - Returns details of a specific course by ID
- **In simple terms:** These are the functions that process what the user requests and return data (views = pages or data endpoints)

#### **`urls.py`**
- **Purpose:** Maps URLs specific to the courses app
- **What it does:** Defines routes within the `/courses/` path:
  - `/courses/` → course_list view
  - `/courses/<id>/` → course_detail view
- **In simple terms:** These are the specific URL patterns for the courses app that get included in the main project URLs

#### **`admin.py`**
- **Purpose:** Configures the Django admin interface
- **What it does:** Registers the `Course` model so it can be managed through `/admin/`:
  - Display fields: name, instructor, credits, created_at
  - Search fields: name, instructor, description
  - Filter options: by credits and creation date
- **In simple terms:** This sets up the admin panel so you can easily add, edit, and delete courses without writing code

#### **`apps.py`**
- **Purpose:** App configuration file
- **What it does:** Configures the `courses` app settings
- **In simple terms:** It's metadata about your app (auto-generated, usually doesn't need editing)

#### **`tests.py`**
- **Purpose:** For writing unit tests for your app
- **What it does:** Empty template for test code
- **In simple terms:** This is where you write tests to verify your code works correctly

#### **`migrations/` folder**
- **Purpose:** Stores database migration files
- **What it does:** Contains `0001_initial.py` which defines the creation of the Course table
- **In simple terms:** These are version control for your database - they track changes to your database schema

---

## How to Use

### 1. **Start the Development Server**
```bash
python manage.py runserver
```
The app will be available at `http://127.0.0.1:8000/`

### 2. **Create an Admin User**
```bash
python manage.py createsuperuser
```
Then visit `http://127.0.0.1:8000/admin/` to add courses

### 3. **Access the API Endpoints**
- **Home:** `http://127.0.0.1:8000/`
- **All Courses:** `http://127.0.0.1:8000/courses/`
- **Course Detail:** `http://127.0.0.1:8000/courses/1/`
- **Admin Panel:** `http://127.0.0.1:8000/admin/`

---

## Summary
This application demonstrates:
- ✅ Database modeling (Course model)
- ✅ Views and URL routing
- ✅ Admin interface
- ✅ API endpoints (JSON responses)
- ✅ Django migrations and database management
