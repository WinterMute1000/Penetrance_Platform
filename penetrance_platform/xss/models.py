from django.db import models


# Create your models here.

# Saved XSS code model
class XSSCode(models.Model):
    xss_code = models.CharField(max_length=2048)

    objects = models.Manager()


# XSS Scan result model
class XSSLog(models.Model):
    host = models.CharField(max_length=2048)
    scan_date = models.DateTimeField(auto_now=True)
    xss_code = models.CharField(max_length=2048)
    result = models.BooleanField()

    objects = models.Manager()
