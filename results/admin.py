from django.contrib import admin
from .models import Result

# Register your models here.
class ResultAdmin(admin.ModelAdmin):
    list_display = ('exam_name',)
    search_fields = ('exam_name',)

admin.site.register(Result, ResultAdmin)
