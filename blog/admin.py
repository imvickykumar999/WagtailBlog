from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')
    readonly_fields = ('name', 'email', 'phone', 'message', 'submitted_at')
    ordering = ['-submitted_at']
