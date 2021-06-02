from django.db import models


# Create your models here.

class FileUploadWebShells(models.Model):
    shell_name = models.CharField(max_length=2048)
    code_or_url = models.CharField(max_length=100000)
    objects = models.Manager()
