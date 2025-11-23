# PDF Management System

A complete Django-based web application for students to upload, download, and manage PDF files with role-based access control and comprehensive student profiles.

## Features

### For Students
- 📤 **Upload & Download PDFs** - Upload PDF files with title and description
- 📥 **Browse PDFs** - View and download all available PDF files
- 👤 **Student Profile** - Comprehensive profile management with:
  - Profile picture upload
  - Personal information (name, email, phone, date of birth)
  - Academic details (student ID, department, year of study)
  - Bio and address
  - Profile completion tracking with visual progress bar
- 📊 **Dashboard Stats** - View upload statistics and recent activity
- 🔐 **Secure Authentication** - Sign up and sign in securely

### For Admins
- 📤 Upload PDF files
- 🗑️ **Delete PDF Files** - Remove PDFs from the system
- 👥 **Manage All PDFs** - Full control over all uploaded files
- 📊 **Admin Dashboard** - Complete management interface

### General Features
- 🔒 **User Authentication** - Secure sign up and sign in
- 👤 **Role-Based Access** - Student and Admin roles with different permissions
- 💅 **Modern Bootstrap UI** - Beautiful, responsive interface with Bootstrap 5
- 🎨 **Gradient Design** - Professional color schemes and animations
- 📱 **Mobile-Friendly** - Fully responsive for all devices
- 🖼️ **Image Upload** - Support for profile pictures with Pillow
- 📈 **Profile Completion** - Track and complete your profile with visual indicators
- 🔔 **Smart Notifications** - Alert system for actions and errors

## Installation

1. Clone the repository:
```bash
git clone https://github.com/surendra767116/pdf.git
cd pdf
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following settings:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create media directories:
```bash
mkdir media
mkdir media/pdfs
mkdir media/profile_pics
```

7. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

8. Start the development server:
```bash
python manage.py runserver
```

9. Open your browser and visit: `http://localhost:8000`

## Usage

### Sign Up
1. Go to the Sign Up page
2. Enter your username, email, and password
3. Click "Sign Up" (all users are created as students by default)
4. You'll be automatically logged in and redirected to the dashboard

### Sign In
1. Go to the Sign In page
2. Enter your credentials
3. Click "Sign In"

### Student Features

#### Dashboard
- Upload PDFs using the upload form
- Browse and download available PDFs
- View PDF details (uploader, size, date)
- See profile completion status with progress bar

#### Profile Management
1. Click "Profile" in the navigation bar
2. View your complete profile with:
   - Profile picture
   - Personal information
   - Academic details
   - Upload statistics
   - Recent activity
3. Click "Edit Profile" to update:
   - Upload profile picture
   - Update personal details
   - Add academic information
   - Write bio and add address
4. Track completion percentage as you fill out your profile

### Admin Dashboard
- All student features plus:
- Delete any PDF file
- Full management control over all uploads
- View all users' uploaded files

### To Make a User Admin
Admin role can only be assigned through Django admin panel:
1. Go to `http://localhost:8000/admin/`
2. Login with superuser credentials
3. Find the user in Users section
4. Change their role to "Admin"

## Project Structure

```
pdf/
├── pdf_manager/         # Main project settings
│   ├── settings.py     # Project configuration
│   ├── urls.py         # Main URL routing
│   └── wsgi.py         # WSGI configuration
├── users/               # User authentication & profiles
│   ├── models.py       # User and StudentProfile models
│   ├── views.py        # Auth and profile views
│   ├── urls.py         # User-related URLs
│   └── migrations/     # Database migrations
├── pdfs/                # PDF management app
│   ├── models.py       # PDF model
│   ├── views.py        # PDF CRUD views
│   └── urls.py         # PDF-related URLs
├── templates/           # HTML templates
│   ├── base.html       # Base template with navbar
│   ├── users/          
│   │   ├── signin.html      # Login page
│   │   ├── signup.html      # Registration page
│   │   ├── profile.html     # Profile view page
│   │   └── edit_profile.html # Profile edit page
│   └── pdfs/           
│       ├── admin_dashboard.html    # Admin dashboard
│       └── student_dashboard.html  # Student dashboard
├── static/             
│   └── css/
│       └── style.css   # Custom CSS styles
├── media/              # User uploaded files
│   ├── pdfs/          # PDF uploads
│   └── profile_pics/  # Profile pictures
├── manage.py
├── requirements.txt
└── README.md
```

## Technologies Used

- **Backend**: Django 4.2.7
- **Database**: SQLite (easily configurable to PostgreSQL/MySQL)
- **Authentication**: Django's built-in authentication system
- **Frontend**: 
  - Bootstrap 5.3.2 (responsive UI framework)
  - Bootstrap Icons (icon library)
  - Custom CSS with gradients and animations
- **Image Processing**: Pillow (profile picture handling)
- **File Handling**: Django FileField with validation
- **Configuration**: python-decouple (environment variables)

## Security Features

- 🔐 **Password Security**: Hashing with Django's default PBKDF2 algorithm
- ✅ **Password Validation**: Strength requirements enforced
- 🛡️ **CSRF Protection**: Built-in protection against cross-site request forgery
- 👥 **Role-Based Access**: Admin role assigned only through Django admin panel
- 📄 **File Validation**: 
  - File type checking (PDF only for documents)
  - File size limits (10MB for PDFs)
  - Content type validation
- 🔒 **Environment Variables**: Sensitive settings in `.env` file
- 🔑 **Session Management**: Secure session handling
- 🚫 **Access Control**: URL-based permission checking

## New Features Added

### Student Profile System
- **Complete Profile Management**: Students can create and manage detailed profiles
- **Profile Picture Upload**: Upload and display custom profile pictures
- **Academic Information**: Track student ID, department, and year of study
- **Personal Details**: Store phone, email, date of birth, and address
- **Bio Section**: Personal description and introduction
- **Profile Completion Tracking**: Visual progress bar showing completion percentage
- **Dashboard Widget**: Smart notifications to complete profile
- **Statistics Display**: View total PDFs uploaded and storage used
- **Recent Activity**: See recently uploaded PDFs from profile page

### Enhanced UI/UX
- **Bootstrap 5 Integration**: Modern, professional interface
- **Responsive Design**: Perfect on all devices (mobile, tablet, desktop)
- **Icon Integration**: Bootstrap Icons throughout the application
- **Gradient Buttons**: Beautiful animated buttons with hover effects
- **Card-Based Layout**: Clean, organized content presentation
- **Progress Indicators**: Visual feedback for profile completion
- **Alert System**: Smart notifications with icons
- **Smooth Animations**: Fade-in, slide-in, and hover effects

### Additional Improvements
- **Profile Navigation**: Quick access to profile from navbar (students only)
- **Edit Profile Page**: Comprehensive form for updating all profile fields
- **Media File Management**: Organized structure for uploads
- **Image Optimization**: Support for various image formats
- **Field Validation**: Smart validation for all input fields
- **Auto Profile Creation**: Profiles automatically created for new students

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

MIT