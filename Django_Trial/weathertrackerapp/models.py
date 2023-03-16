from django.db import models
from datetime import datetime

# Create your models here.
class Query(models.Model):
    location = models.CharField(max_length=50)
    createdAt = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.location