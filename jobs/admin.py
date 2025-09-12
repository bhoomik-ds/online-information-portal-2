from django.contrib import admin
from .models import Job, QuickLink, CallLetter, AdmitCard
from notifications.models import Notification

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization_name', 'post_name', 'salary', 'total_vacancies', 'start_date', 'end_date', 'created_at')
    list_filter = ('organization_name', 'created_at')
    search_fields = ('title', 'organization_name', 'post_name')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'short_description', 'image')
        }),
        ('Organization Details', {
            'fields': ('organization_name', 'post_name', 'salary', 'total_vacancies')
        }),
        ('Application Dates', {
            'fields': ('start_date', 'end_date'),
            'description': 'Enter dates in text format (e.g., "15/09/2025" or "15 September 2025")'
        }),
        ('Qualification & Requirements', {
            'fields': ('education_qualification', 'age_limit', 'application_fee', 'exam_pattern'),
            'description': 'For Exam Pattern: You can create tables using HTML for better formatting.'
        }),
        ('Links Section', {
            'fields': ('apply_online_link', 'official_notification_link', 'whatsapp_link', 'telegram_link', 'youtube_link'),
            'classes': ('collapse',),
            'description': 'Add relevant links for this job posting'
        })
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('created_at', 'updated_at')
        return ()
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['image'].label = 'Image Upload'
        return form

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'order', 'created_at')
    search_fields = ('title', 'short_description')
    ordering = ('order', '-created_at')

admin.site.register(Job, JobAdmin)
admin.site.register(QuickLink)
admin.site.register(CallLetter)
admin.site.register(AdmitCard)
