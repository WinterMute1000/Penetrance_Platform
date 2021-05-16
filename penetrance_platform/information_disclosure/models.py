from django.db import models


# Create your models here.

class InformationDisclosureLog(models.Model):
    host = models.CharField(max_length=2048)
    scan_date = models.DateTimeField(auto_now=True)
    result = models.TextField()

    objects = models.Manager()

    def is_valid(self):
        host = self.data['host']

        if len(host) > 2048 or host is None:
            return False

        return True
