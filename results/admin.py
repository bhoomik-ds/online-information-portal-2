from django.contrib import admin
from .models import Result

# Register your models here.
class ResultAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order')
    search_fields = ('title',)

admin.site.register(Result, ResultAdmin)
