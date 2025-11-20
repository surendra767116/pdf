from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse, Http404
from .models import PDF
import os

@login_required
def student_dashboard_view(request):
    pdfs = PDF.objects.all()
    return render(request, 'pdfs/student_dashboard.html', {'pdfs': pdfs})

@login_required
def admin_dashboard_view(request):
    if request.user.role != 'admin':
        messages.error(request, 'Access denied! Admin only.')
        return redirect('student_dashboard')
    
    pdfs = PDF.objects.all()
    return render(request, 'pdfs/admin_dashboard.html', {'pdfs': pdfs})

@login_required
def upload_pdf_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        file = request.FILES.get('file')
        
        if not file:
            messages.error(request, 'Please select a PDF file!')
            return redirect(request.META.get('HTTP_REFERER', 'dashboard'))
        
        if not file.name.endswith('.pdf'):
            messages.error(request, 'Only PDF files are allowed!')
            return redirect(request.META.get('HTTP_REFERER', 'dashboard'))
        
        pdf = PDF.objects.create(
            title=title,
            description=description,
            file=file,
            uploaded_by=request.user,
            file_size=file.size
        )
        
        messages.success(request, f'PDF "{title}" uploaded successfully!')
        return redirect(request.META.get('HTTP_REFERER', 'dashboard'))
    
    return redirect('dashboard')

@login_required
def download_pdf_view(request, pdf_id):
    pdf = get_object_or_404(PDF, id=pdf_id)
    
    try:
        return FileResponse(pdf.file.open('rb'), as_attachment=True, filename=pdf.file.name.split('/')[-1])
    except FileNotFoundError:
        raise Http404("PDF file not found")

@login_required
def delete_pdf_view(request, pdf_id):
    if request.user.role != 'admin':
        messages.error(request, 'Access denied! Admin only.')
        return redirect('student_dashboard')
    
    pdf = get_object_or_404(PDF, id=pdf_id)
    
    # Delete the file from storage
    if pdf.file and os.path.isfile(pdf.file.path):
        os.remove(pdf.file.path)
    
    pdf.delete()
    messages.success(request, f'PDF "{pdf.title}" deleted successfully!')
    return redirect('admin_dashboard')
