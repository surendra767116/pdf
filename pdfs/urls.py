from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_dashboard_view, name='student_dashboard'),
    path('admin/', views.admin_dashboard_view, name='admin_dashboard'),
    path('upload/', views.upload_pdf_view, name='upload_pdf'),
    path('download/<int:pdf_id>/', views.download_pdf_view, name='download_pdf'),
    path('delete/<int:pdf_id>/', views.delete_pdf_view, name='delete_pdf'),
]
