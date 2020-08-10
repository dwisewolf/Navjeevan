from django.db import models
import json
import jsonfield


# Create your models here.

class Vimeo(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    college = models.CharField(max_length=100, null=True, blank=True)
    sub = models.CharField(max_length=100, null=True, blank=True)
    data = jsonfield.JSONField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title


class VimeoStatus(models.Model):
    status = models.BooleanField(default=False)
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
