from django.db import models


# Create your models here.

# Saved XXE code model
class XXECode(models.Model):
    xxe_code = models.CharField(max_length=2048)
    objects = models.Manager()


# XXE Scan result model
class XXELog(models.Model):
    host = models.CharField(max_length=2048)
    scan_date = models.DateTimeField(auto_now=True)
    xxe_code = models.CharField(max_length=2048)
    result = models.BooleanField()

    objects = models.Manager()
