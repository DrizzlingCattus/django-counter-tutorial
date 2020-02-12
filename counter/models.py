import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Counter(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    count = models.IntegerField(default=0)
    time_limit = models.DateTimeField(default=timezone.now() + datetime.timedelta(seconds=60))
    # n = normal, e = expired
    status = models.CharField(default="n", max_length=4)

    def __str__(self):
        limit = self.time_limit - timezone.now()
        return f'[{self.pub_date}] [{self.status}] counts : {self.count} ({limit})'

