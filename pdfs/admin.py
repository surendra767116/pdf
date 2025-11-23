from django.contrib import admin
from .models import PDF

@admin.register(PDF)
class PDFAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'file_size', 'uploaded_at')
    list_filter = ('uploaded_at', 'uploaded_by')
    search_fields = ('title', 'description')
    readonly_fields = ('uploaded_at', 'file_size')
