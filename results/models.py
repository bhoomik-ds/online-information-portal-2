from django.db import models

# Create your models here.

class Result(models.Model):
    exam_name = models.CharField(max_length=255)
    # result_date removed
    result_file = models.FileField(upload_to='results/', blank=True, null=True)

    def __str__(self):
        return self.exam_name
