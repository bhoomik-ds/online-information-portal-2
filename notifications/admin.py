from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'short_description', 'image',
        'organization_name', 'post_name', 'salary', 'total_vacancies',
        'start_date', 'end_date',
        'education_qualification', 'age_limit', 'application_fee', 'exam_pattern',
        'apply_online_link', 'official_notification_link', 'whatsapp_link', 'telegram_link', 'youtube_link',
        'order'
    )
    search_fields = ('title', 'organization_name', 'post_name')
    list_filter = ('order', 'organization_name', 'start_date')

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
        }),
        ('Order', {
            'fields': ('order',)
        })
    )

admin.site.register(Notification, NotificationAdmin)
