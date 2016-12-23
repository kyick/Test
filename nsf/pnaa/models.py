from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Route(models.Model):
    title = models.CharField(max_length=200)
    starting_point = models.TextField()
    destination = models.TextField()
    critical_points_count = models.IntegerField()
    critical_points_list = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Cell(models.Model):
    title = models.CharField(max_length=200)
    cellid = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, blank=True)
    
    def __str__(self):
        return self.title

