# PDF Management System - Setup Guide

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/surendra767116/pdf.git
   cd pdf
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

4. **(Optional) Create a superuser for Django admin**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your browser and go to: `http://localhost:8000`
   - You'll be redirected to the sign-in page
   - Click "Sign Up" to create a new account

## User Guide

### Creating an Account

1. Click "Sign Up" on the homepage
2. Fill in the form:
   - Username (required, unique)
   - Email (required, unique)
   - Password (required)
   - Confirm Password (must match)
   - Role: Choose "Student" or "Admin"
3. Click "Sign Up"
4. You'll be redirected to the sign-in page

### Signing In

1. Enter your username and password
2. Click "Sign In"
3. You'll be redirected to your dashboard based on your role

### Student Dashboard

**Upload a PDF:**
1. Fill in the title (required)
2. Click "Choose File" and select a PDF
3. (Optional) Add a description
4. Click "Upload PDF"

**Download a PDF:**
1. Scroll to the "Available PDFs" section
2. Click the green "Download" button on any PDF card

**View PDF Details:**
- Each PDF card shows:
  - Title
  - Uploader
  - File size
  - Upload date
  - Description (if provided)

### Admin Dashboard

Admins have all student features plus:

**Delete a PDF:**
1. Scroll to the "All PDFs" section
2. Click the red "Delete" button on any PDF card
3. Confirm the deletion in the popup dialog

### Signing Out

Click "Sign Out" in the top-right corner of any page.

## Features

### Authentication
- ✅ Secure password hashing
- ✅ Session-based authentication
- ✅ Role-based access control
- ✅ CSRF protection

### File Management
- ✅ PDF upload with validation
- ✅ File size tracking
- ✅ Secure file storage
- ✅ Download functionality
- ✅ Admin-only deletion

### User Interface
- ✅ Responsive design (works on mobile, tablet, desktop)
- ✅ Modern gradient theme
- ✅ Intuitive navigation
- ✅ Success/error notifications
- ✅ Card-based PDF display

## Configuration

### Changing the Database

By default, the app uses SQLite. To use PostgreSQL or MySQL:

1. Install the appropriate database adapter:
   ```bash
   # For PostgreSQL
   pip install psycopg2-binary
   
   # For MySQL
   pip install mysqlclient
   ```

2. Update `pdf_manager/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',  # or mysql
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',  # or 3306 for MySQL
       }
   }
   ```

3. Run migrations again:
   ```bash
   python manage.py migrate
   ```

### Changing Upload Settings

Edit `pdf_manager/settings.py`:

```python
# Maximum upload file size (in bytes)
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10 MB

# Media files location
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'
```

### Production Deployment

For production:

1. Set `DEBUG = False` in `settings.py`
2. Set `ALLOWED_HOSTS` to your domain
3. Generate a new `SECRET_KEY`
4. Use a production database (PostgreSQL recommended)
5. Configure a production web server (Gunicorn + Nginx)
6. Set up static file serving:
   ```bash
   python manage.py collectstatic
   ```

## Troubleshooting

### "No such file or directory" error
Make sure you're in the project directory when running commands.

### "Port already in use" error
Either stop the process using port 8000, or run on a different port:
```bash
python manage.py runserver 8080
```

### File upload not working
1. Check that the `media` folder exists and is writable
2. Verify file is a valid PDF
3. Check file size is under the limit

### Can't sign in
1. Verify you created an account
2. Check username/password are correct
3. Ensure migrations were run

## Support

For issues or questions:
1. Check this guide first
2. Review the README.md
3. Open an issue on GitHub

## License

MIT License - see LICENSE file for details
