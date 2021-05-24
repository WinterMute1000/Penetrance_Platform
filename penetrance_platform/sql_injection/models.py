from django.db import models


# Create your models here.

# Saved SQL Injection code model
class SQLInjectionCode(models.Model):
    sql_true_code = models.CharField(max_length=2048)
    sql_false_code = models.CharField(max_length=2048)
    objects = models.Manager()


# XSS Scan result model
class SQLInjectionLog(models.Model):
    host = models.CharField(max_length=2048)
    scan_date = models.DateTimeField(auto_now=True)
    sql_injection_code = models.CharField(max_length=2048)
    result = models.BooleanField()

    objects = models.Manager()
