from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order')
    search_fields = ('title',)
    list_filter = ('order',)

admin.site.register(Notification, NotificationAdmin)
