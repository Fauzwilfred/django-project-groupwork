# Quick Reference: Django File Guide

## Understanding Django's Architecture

### **The Three-Part System: Models, Views, URLs**

Django follows the **Model-View-URL** pattern:
1. **Models** → Define what data looks like (database structure)
2. **Views** → Define how to handle requests (process data)
3. **URLs** → Define which page handles which request (routing)

---

## File Breakdown by Category

### 🗄️ **Database Files**

| File | Purpose |
|------|---------|
| `courses/models.py` | Defines the Course database structure with fields like name, instructor, credits |
| `courses/migrations/` | History of database changes (auto-generated when you make model changes) |
| `db.sqlite3` | The actual database file (created after migrations) |

### 👁️ **Request Handling Files**

| File | Purpose |
|------|---------|
| `courses/views.py` | Functions that process requests and return responses (home, course_list, course_detail) |
| `student_app/urls.py` | Main URL router (directs `/` to home, `/courses/` to course_list, etc.) |
| `courses/urls.py` | App-specific URL patterns |

### ⚙️ **Configuration Files**

| File | Purpose |
|------|---------|
| `student_app/settings.py` | Project configuration (database, installed apps, security) |
| `student_app/wsgi.py` | Deployment configuration for web servers |
| `student_app/asgi.py` | Configuration for async/WebSocket support |

### 🔧 **Management Files**

| File | Purpose |
|------|---------|
| `manage.py` | Command-line tool to manage the project |
| `courses/admin.py` | Registers models in Django admin panel for easy management |
| `courses/apps.py` | App configuration metadata |

---

## Common Commands

```bash
# Start the development server
python manage.py runserver

# Create a superuser (admin account)
python manage.py createsuperuser

# Make changes to models, then run:
python manage.py makemigrations
python manage.py migrate

# Create a new app
python manage.py startapp appname

# Open the Django shell (interactive Python with your models)
python manage.py shell
```

---

## How Requests Flow Through the System

```
User visits: http://127.0.0.1:8000/courses/1/
                ↓
        urls.py checks the URL
                ↓
        Finds pattern: courses/<int:course_id>/
                ↓
        Routes to: views.course_detail(request, course_id=1)
                ↓
        View function queries: Course.objects.get(id=1)
                ↓
        Model returns data from database
                ↓
        View formats as JSON response
                ↓
        Browser receives and displays data
```

---

## Next Steps to Expand Your App

### ✅ What You Have Now:
- Course model with fields
- List and detail views
- Admin interface to manage courses
- API endpoints that return JSON

### 📋 To-Do for Features:
1. **Add Templates** - Create HTML files in `courses/templates/` to show data nicely
2. **Add More Models** - Create Student, Enrollment models
3. **Add Forms** - Create forms to allow users to submit course data
4. **Add Permissions** - Control who can view/edit/delete courses
5. **Add Tests** - Write tests in `courses/tests.py`
6. **Deploy** - Move to production using a proper server

---

## Key Django Concepts

| Term | Meaning |
|------|---------|
| **App** | A module that provides functionality (courses, students, etc.) |
| **Model** | A Python class that represents a database table |
| **View** | A function/class that handles requests and returns responses |
| **URL Pattern** | A mapping from a URL path to a view function |
| **Migration** | A file that describes database changes |
| **QuerySet** | A database query that returns a list of objects |
| **Template** | An HTML file with dynamic content |
| **Admin** | The built-in Django interface to manage data |

---

## File Locations Reference

```
student_app/                          ← Main project directory
├── manage.py                         ← Start here for commands
├── db.sqlite3                        ← Your database file
├── student_app/                      ← Project config folder
│   ├── settings.py                   ← Edit here to add apps
│   ├── urls.py                       ← Main URL routes
│   ├── wsgi.py                       ← Production deployment
│   └── asgi.py                       ← Async support
└── courses/                          ← Your first app
    ├── models.py                     ← Define Course class here
    ├── views.py                      ← Define page handlers here
    ├── urls.py                       ← Define routes here
    ├── admin.py                      ← Manage in Django admin
    ├── migrations/                   ← Database history
    │   └── 0001_initial.py
    └── apps.py                       ← App configuration
```
