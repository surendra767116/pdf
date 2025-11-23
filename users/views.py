from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import User, StudentProfile
from pdfs.models import PDF


def home_view(request):
    """Public landing page with marketing content."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    feature_cards = [
        {
            'icon': 'bi-cloud-arrow-up-fill',
            'title': 'Frictionless Uploads',
            'text': 'Drag, drop, and publish polished study material in seconds with server-side validation.',
            'chip': 'New'
        },
        {
            'icon': 'bi-shield-lock-fill',
            'title': 'Enterprise-Grade Security',
            'text': 'Role-based permissions, audit-ready logs, and OWASP-aligned safeguards keep IP protected.',
            'chip': 'Secure'
        },
        {
            'icon': 'bi-speedometer',
            'title': 'Lightning Performance',
            'text': 'Optimized storage, smart caching, and instant previews provide a delightful browsing experience.',
            'chip': 'Fast'
        }
    ]

    timeline_steps = [
        {
            'step': '01',
            'title': 'Create your workspace',
            'text': 'Sign up in under a minute and invite your peers or faculty collaborators.'
        },
        {
            'step': '02',
            'title': 'Upload curated PDFs',
            'text': 'Tag, describe, and publish documents with structured metadata and instant validation.'
        },
        {
            'step': '03',
            'title': 'Share and track',
            'text': 'Deliver a consumer-grade reading experience while tracking engagement and downloads.'
        }
    ]

    testimonials = [
        {
            'quote': '“The PDF Manager replaced three tools for our academic cohort. Uploads are fast, and approvals are transparent.”',
            'author': 'Aarav Kulkarni',
            'role': 'Program Coordinator, SkillForge'
        },
        {
            'quote': '“Our students finally have a single source of truth for course packs, and the UI feels on par with any SaaS product.”',
            'author': 'Dr. Meera Patel',
            'role': 'Dean of Academics, NextGen University'
        }
    ]

    stats = {
        'pdf_count': PDF.objects.count(),
        'student_count': User.objects.filter(role='student').count(),
        'uptime': '99.9%'
    }

    context = {
        'feature_cards': feature_cards,
        'timeline_steps': timeline_steps,
        'testimonials': testimonials,
        'stats': stats,
    }

    return render(request, 'home.html', context)

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'users/signup.html')
        
        # Validate password strength
        try:
            validate_password(password)
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)
            return render(request, 'users/signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'users/signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return render(request, 'users/signup.html')
        
        # Always create users as 'student' - admin role must be assigned through Django admin
        user = User.objects.create_user(username=username, email=email, password=password, role='student')
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('dashboard')
    
    return render(request, 'users/signup.html')

def signin_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Your account is inactive!')
        else:
            messages.error(request, 'Invalid username or password!')
    
    return render(request, 'users/signin.html')

@login_required
def signout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('signin')

@login_required
def dashboard_view(request):
    if request.user.role == 'admin':
        return redirect('admin_dashboard')
    else:
        return redirect('student_dashboard')


@login_required
def profile_view(request):
    """View student profile"""
    if request.user.role != 'student':
        messages.warning(request, 'Profile feature is only available for students.')
        return redirect('dashboard')
    
    profile, created = StudentProfile.objects.get_or_create(user=request.user)
    
    # Get user's uploaded PDFs
    user_pdfs = PDF.objects.filter(uploaded_by=request.user).order_by('-uploaded_at')
    
    # Calculate statistics
    total_pdfs = user_pdfs.count()
    total_size = sum(pdf.file_size for pdf in user_pdfs)
    
    context = {
        'profile': profile,
        'user_pdfs': user_pdfs[:5],  # Show last 5 PDFs
        'total_pdfs': total_pdfs,
        'total_size': total_size,
    }
    
    return render(request, 'users/profile.html', context)


@login_required
def edit_profile_view(request):
    """Edit student profile"""
    if request.user.role != 'student':
        messages.warning(request, 'Profile feature is only available for students.')
        return redirect('dashboard')
    
    profile, created = StudentProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Update user fields
        request.user.first_name = request.POST.get('first_name', '').strip()
        request.user.last_name = request.POST.get('last_name', '').strip()
        request.user.email = request.POST.get('email', '').strip()
        
        # Update profile fields
        profile.full_name = request.POST.get('full_name', '').strip()
        profile.phone = request.POST.get('phone', '').strip()
        profile.student_id = request.POST.get('student_id', '').strip() or None
        profile.department = request.POST.get('department', '').strip()
        profile.year_of_study = request.POST.get('year_of_study', '').strip()
        profile.bio = request.POST.get('bio', '').strip()
        profile.address = request.POST.get('address', '').strip()
        
        # Handle date of birth
        dob = request.POST.get('date_of_birth', '').strip()
        if dob:
            profile.date_of_birth = dob
        
        # Handle profile picture
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        
        try:
            request.user.save()
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        except Exception as e:
            messages.error(request, f'Error updating profile: {str(e)}')
    
    context = {
        'profile': profile,
    }
    
    return render(request, 'users/edit_profile.html', context)
