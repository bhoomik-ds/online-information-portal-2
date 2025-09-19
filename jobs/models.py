from django.db import models
class CallLetter(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=500)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class AdmitCard(models.Model):
    # Basic Information
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    from cloudinary_storage.storage import MediaCloudinaryStorage
    image = models.ImageField(upload_to='upcoming_job_images/', blank=True, null=True, storage=MediaCloudinaryStorage())
    
    # Organization Details
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    post_name = models.CharField(max_length=255, blank=True, null=True)
    salary = models.TextField(blank=True, null=True)
    total_vacancies = models.CharField(max_length=100, blank=True, null=True)
    
    # Application Dates
    start_date = models.CharField(max_length=50, blank=True, null=True)
    end_date = models.CharField(max_length=50, blank=True, null=True)
    
    # Qualification Details
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
    
    # Metadata
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Upcoming Job'
        verbose_name_plural = 'Upcoming Jobs'

    def __str__(self):
        return self.title

class Job(models.Model):
    # Basic Information
    title = models.CharField(max_length=255, verbose_name="Title")
    short_description = models.TextField(verbose_name="Short Description", blank=True, null=True)
    from cloudinary_storage.storage import MediaCloudinaryStorage
    image = models.ImageField(upload_to='job_images/', blank=True, null=True, storage=MediaCloudinaryStorage())
    
    # Organization Details
    organization_name = models.CharField(max_length=255, verbose_name="Organization Name", blank=True, null=True)
    post_name = models.CharField(max_length=255, verbose_name="Post Name", blank=True, null=True)
    salary = models.TextField(verbose_name="Salary", blank=True, null=True)
    total_vacancies = models.CharField(max_length=100, verbose_name="Total Vacancies", blank=True, null=True)
    
    # Application Dates
    start_date = models.CharField(max_length=50, verbose_name="Application Start Date", blank=True, null=True)
    end_date = models.CharField(max_length=50, verbose_name="Application End Date", blank=True, null=True)
    
    # Qualification Details
    education_qualification = models.TextField(verbose_name="Education Qualification", blank=True, null=True)
    age_limit = models.CharField(max_length=100, verbose_name="Age Limit", blank=True, null=True)
    application_fee = models.CharField(max_length=100, verbose_name="Application Fee", blank=True, null=True)
    exam_pattern = models.TextField(verbose_name="Exam Pattern", blank=True, null=True)
    
    # Links Section
    apply_online_link = models.URLField(max_length=500, verbose_name="Apply Online", blank=True, null=True)
    official_notification_link = models.URLField(max_length=500, verbose_name="Official Notification", blank=True, null=True)
    whatsapp_link = models.URLField(max_length=500, verbose_name="WhatsApp Channel", blank=True, null=True)
    telegram_link = models.URLField(max_length=500, verbose_name="Telegram Channel", blank=True, null=True)
    youtube_link = models.URLField(max_length=500, verbose_name="YouTube Channel", blank=True, null=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Job"
        verbose_name_plural = "Jobs"
    
    def __str__(self):
        return self.title

class QuickLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=500)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


