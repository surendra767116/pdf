from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse, Http404
from django.core.paginator import Paginator
from .models import PDF
import os

@login_required
def student_dashboard_view(request):
    pdfs = PDF.objects.select_related('uploaded_by').all()
    
    # Get profile completion status for students
    profile_completion = None
    if request.user.role == 'student':
        try:
            from users.models import StudentProfile
            profile = StudentProfile.objects.get(user=request.user)
            
            # Calculate profile completion percentage
            fields = [
                profile.full_name,
                profile.phone,
                profile.student_id,
                profile.department,
                profile.year_of_study,
                profile.bio,
                profile.date_of_birth,
                profile.profile_picture,
            ]
            completed_fields = sum(1 for field in fields if field)
            profile_completion = int((completed_fields / len(fields)) * 100)
        except:
            profile_completion = 0
    
    context = {
        'pdfs': pdfs,
        'profile_completion': profile_completion,
    }
    return render(request, 'pdfs/student_dashboard.html', context)

@login_required
def admin_dashboard_view(request):
    if request.user.role != 'admin':
        messages.error(request, 'Access denied! Admin only.')
        return redirect('student_dashboard')
    
    pdfs = PDF.objects.select_related('uploaded_by').all()
    return render(request, 'pdfs/admin_dashboard.html', {'pdfs': pdfs})

@login_required
def upload_pdf_view(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()[:255]
        description = request.POST.get('description', '').strip()[:1000]
        file = request.FILES.get('file')
        
        if not title:
            messages.error(request, 'Title is required!')
            redirect_url = 'admin_dashboard' if request.user.role == 'admin' else 'student_dashboard'
            return redirect(redirect_url)
        
        if not file:
            messages.error(request, 'Please select a PDF file!')
            redirect_url = 'admin_dashboard' if request.user.role == 'admin' else 'student_dashboard'
            return redirect(redirect_url)
        
        # Validate file extension and content type
        if not file.name.lower().endswith('.pdf') or file.content_type != 'application/pdf':
            messages.error(request, 'Only PDF files are allowed!')
            redirect_url = 'admin_dashboard' if request.user.role == 'admin' else 'student_dashboard'
            return redirect(redirect_url)
        
        # Validate file size (10MB limit)
        MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
        if file.size > MAX_FILE_SIZE:
            messages.error(request, 'File size exceeds 10MB limit!')
            redirect_url = 'admin_dashboard' if request.user.role == 'admin' else 'student_dashboard'
            return redirect(redirect_url)
        
        PDF.objects.create(
            title=title,
            description=description,
            file=file,
            uploaded_by=request.user,
            file_size=file.size
        )
        
        messages.success(request, f'PDF "{title}" uploaded successfully!')
        redirect_url = 'admin_dashboard' if request.user.role == 'admin' else 'student_dashboard'
        return redirect(redirect_url)
    
    return redirect('dashboard')

@login_required
def download_pdf_view(request, pdf_id):
    pdf = get_object_or_404(PDF, id=pdf_id)
    
    try:
        return FileResponse(pdf.file.open('rb'), as_attachment=True, filename=os.path.basename(pdf.file.name))
    except FileNotFoundError:
        raise Http404("PDF file not found")

@login_required
def delete_pdf_view(request, pdf_id):
    if request.user.role != 'admin':
        messages.error(request, 'Access denied! Admin only.')
        return redirect('student_dashboard')
    
    pdf = get_object_or_404(PDF, id=pdf_id)
    title = pdf.title
    
    # Delete the file from storage using Django's storage system
    try:
        pdf.file.delete(save=False)
    except Exception:
        pass  # Continue with database deletion even if file deletion fails
    
    pdf.delete()
    messages.success(request, f'PDF "{title}" deleted successfully!')
    return redirect('admin_dashboard')
