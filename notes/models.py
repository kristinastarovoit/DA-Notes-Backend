from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=300)
    marked = models.BooleanField(default=False)
    trash = models.BooleanField(default=False)
