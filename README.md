# PDF Management System

A complete Django-based web application for students to upload, download, and manage PDF files with role-based access control.

## Features

### For Students
- 📤 Upload PDF files with title and description
- 📥 Download available PDF files
- 📚 View all uploaded PDFs
- 🔐 Secure authentication

### For Admins
- 📤 Upload PDF files
- 🗑️ Delete PDF files
- 👥 Manage all PDFs from all users
- 📊 Admin dashboard with full control

### General Features
- 🔒 User authentication (Sign up / Sign in)
- 👤 Role-based access control (Student / Admin)
- 💅 Modern and responsive UI
- 🎨 Beautiful gradient design
- 📱 Mobile-friendly interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/surendra767116/pdf.git
cd pdf
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open your browser and visit: `http://localhost:8000`

## Usage

### Sign Up
1. Go to the Sign Up page
2. Enter your username, email, and password
3. Select your role (Student or Admin)
4. Click "Sign Up"

### Sign In
1. Go to the Sign In page
2. Enter your credentials
3. Click "Sign In"

### Student Dashboard
- Upload PDFs using the upload form
- Browse and download available PDFs
- View PDF details (uploader, size, date)

### Admin Dashboard
- All student features plus:
- Delete any PDF file
- Full management control

## Project Structure

```
pdf/
├── pdf_manager/         # Main project settings
├── users/               # User authentication app
├── pdfs/                # PDF management app
├── templates/           # HTML templates
│   ├── base.html
│   ├── users/          # Auth templates
│   └── pdfs/           # Dashboard templates
├── static/             # Static files (CSS, JS)
├── media/              # Uploaded files
├── manage.py
└── requirements.txt
```

## Technologies Used

- **Backend**: Django 4.2.7
- **Database**: SQLite (can be changed to PostgreSQL/MySQL)
- **Authentication**: Django Auth with JWT support
- **Frontend**: HTML, CSS (modern gradient design)
- **File Handling**: Django FileField

## Security Features

- Password hashing with bcrypt
- CSRF protection
- Role-based access control
- Secure file upload validation
- Session management

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

MIT