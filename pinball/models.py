from django.db import models
from django.utils import timezone

class Score(models.Model):
    high_score = models.BigIntegerField(default=0)
    username = models.CharField(max_length=50)
    date = models.DateTimeField('Date published', default=timezone.now())