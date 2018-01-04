from django.db import models
import datetime
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title +"\n"+self.body
    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)
