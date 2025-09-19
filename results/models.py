from django.db import models

# Create your models here.

class Result(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=500, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
