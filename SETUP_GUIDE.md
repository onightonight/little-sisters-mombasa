# Django CMS for Little Sisters of the Poor - Mombasa

## 🚀 Quick Start Guide

This is a complete Django-based Content Management System (CMS) for the Little Sisters of the Poor website. It allows you to:

- ✅ Add and manage photos in a beautiful gallery
- ✅ Post blog updates and news
- ✅ Manage the website through an easy admin panel
- ✅ Display dynamic content on different pages

---

## 📋 Prerequisites

Before you start, make sure you have:

- **Python 3.8+** installed ([Download here](https://www.python.org/downloads/))
- **pip** (comes with Python)
- A text editor like VS Code or Notepad++
- About 500MB of free disk space

Check if Python is installed:
```bash
python --version
# or
python3 --version
```

---

## 🔧 Installation Steps

### Step 1: Create a Virtual Environment

A virtual environment keeps your project dependencies isolated.

**On Windows:**
```bash
cd little_sisters_project
python -m venv venv
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
cd little_sisters_project
python3 -m venv venv
source venv/bin/activate
```

After activation, you'll see `(venv)` at the start of your terminal line.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs Django, REST Framework, and all other packages needed.

### Step 3: Set Up Environment Variables

Copy the example file and customize it:

```bash
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
```

Edit the `.env` file with your settings:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Step 4: Create Database Tables

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates the database and tables for photos, blog posts, etc.

### Step 5: Create Admin User

Create a superuser account to access the admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts:
- Username: admin (or your choice)
- Email: your-email@example.com
- Password: (create a strong password)

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

---

## 🌐 Accessing Your Website

### Frontend (Public Pages)
- **Homepage**: http://localhost:8000/
- **Gallery**: http://localhost:8000/gallery/
- **Blog/Updates**: http://localhost:8000/blog/

### Admin Panel (Content Management)
- **Admin Login**: http://localhost:8000/admin/
- Username: `admin`
- Password: (the one you created)

---

## 📸 How to Add Photos

1. Go to http://localhost:8000/admin/
2. Click on **Photos** in the left menu
3. Click **Add Photo**
4. Fill in the details:
   - **Title**: Name of the photo (e.g., "Volunteers Helping Elders")
   - **Description**: Brief description
   - **Image**: Upload the photo file
   - **Category**: Select (Elders, Volunteers, Events, Facilities, Community)
   - **Photographer**: Name of who took the photo
   - **Date Taken**: When the photo was taken
   - **Featured**: Check this to show on homepage
   - **Is Published**: Check to make visible on website
5. Click **Save**

Photos will automatically appear on:
- Homepage gallery section
- Full gallery page: /gallery/

---

## 📝 How to Write Blog Posts

1. Go to http://localhost:8000/admin/
2. Click on **Blog Posts** in the left menu
3. Click **Add Blog Post**
4. Fill in the details:
   - **Title**: Article title
   - **Slug**: URL-friendly version (auto-filled)
   - **Author**: Select yourself
   - **Excerpt**: Short summary (appears in listings)
   - **Content**: Full article text (HTML supported)
   - **Featured Image**: Optional cover photo
   - **Status**: Set to "Published" to make visible
   - **Tags**: Comma-separated keywords (e.g., "elders, care, news")
   - **Allow Comments**: Check if you want comments
5. Click **Publish** or **Save**

Blog posts will appear on:
- Homepage recent updates section
- Full blog page: /blog/
- Individual article pages: /blog/article-title/

---

## 🗂️ Project Structure

```
little_sisters_project/
├── manage.py                 # Main Django command file
├── requirements.txt          # List of dependencies
├── .env.example             # Environment variables template
├── db.sqlite3               # Database (created after first run)
├── config/
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Website routes
│   ├── asgi.py              # Server config
│   └── wsgi.py              # Server config
├── core/
│   ├── models.py            # Database models
│   ├── views.py             # API endpoints
│   ├── page_views.py        # Page rendering
│   ├── admin.py             # Admin panel customization
│   ├── urls.py              # API routes
│   └── serializers.py       # API data formatting
└── templates/
    ├── index.html           # Homepage
    ├── gallery.html         # Photo gallery page
    ├── blog.html            # Blog listing
    └── blog-detail.html     # Individual article
```

---

## 🛡️ Important: Security Settings

### For Development (Current Setup)
Your website runs in DEBUG mode with default settings. This is fine for testing locally.

### For Production (When Going Live)

Before deploying to the internet, change these in `.env`:

```
DEBUG=False
SECRET_KEY=generate-a-real-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

Generate a secure SECRET_KEY:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

---

## 📚 Useful Commands

### Start the server
```bash
python manage.py runserver
```

### Create new admin user
```bash
python manage.py createsuperuser
```

### Check for issues
```bash
python manage.py check
```

### See all database tables
```bash
python manage.py showmigrations
```

### Stop the server
Press `Ctrl + C` in the terminal

### Deactivate virtual environment
```bash
deactivate
```

---

## 🚨 Troubleshooting

### "ModuleNotFoundError: No module named 'django'"
- Make sure your virtual environment is activated (you should see `(venv)` in terminal)
- Run: `pip install -r requirements.txt`

### "Port 8000 is already in use"
```bash
python manage.py runserver 8001  # Use different port
```

### "No such table" errors
- Run: `python manage.py migrate`

### Admin panel looks plain (no styling)
- Run: `python manage.py collectstatic --noinput`

### Can't upload images
- Check that `media/` folder exists in project root
- Check file permissions
- Make sure image file is under 10MB

### Forgot admin password
```bash
python manage.py changepassword admin
```

---

## 🌐 Deploying to Production

When you're ready to go live, you'll need to:

1. **Choose a hosting provider**: PythonAnywhere, Heroku, DigitalOcean, AWS, etc.
2. **Use PostgreSQL** instead of SQLite (better for production)
3. **Set up HTTPS** (SSL certificate)
4. **Configure email** for notifications
5. **Use a production server** like Gunicorn + Nginx

For detailed deployment instructions, see: `DEPLOYMENT.md` (coming soon)

---

## 📞 Support

For issues or questions:
- Check Django documentation: https://docs.djangoproject.com/
- REST Framework docs: https://www.django-rest-framework.org/
- Django community: https://www.djangoproject.com/community/

---

## 📄 License

This project is created for Little Sisters of the Poor, Mombasa.

---

## Version History

- **v1.0** (March 2025): Initial release with photo gallery and blog functionality
