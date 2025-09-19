from django.db import models

# Create your models here.

class Notification(models.Model):
    # Basic Information
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    from cloudinary_storage.storage import MediaCloudinaryStorage
    image = models.ImageField(upload_to='notification_images/', blank=True, null=True, storage=MediaCloudinaryStorage())

    # Organization Details
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    post_name = models.CharField(max_length=255, blank=True, null=True)
    salary = models.TextField(blank=True, null=True)
    total_vacancies = models.CharField(max_length=100, blank=True, null=True)

    # Application Dates
    start_date = models.CharField(max_length=50, blank=True, null=True)
    end_date = models.CharField(max_length=50, blank=True, null=True)

    # Qualification & Requirements
    education_qualification = models.TextField(blank=True, null=True)
    age_limit = models.CharField(max_length=100, blank=True, null=True)
    application_fee = models.CharField(max_length=100, blank=True, null=True)
    exam_pattern = models.TextField(blank=True, null=True)

    # Links Section
    apply_online_link = models.URLField(max_length=500, blank=True, null=True)
    official_notification_link = models.URLField(max_length=500, blank=True, null=True)
    whatsapp_link = models.URLField(max_length=500, blank=True, null=True)
    telegram_link = models.URLField(max_length=500, blank=True, null=True)
    youtube_link = models.URLField(max_length=500, blank=True, null=True)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
