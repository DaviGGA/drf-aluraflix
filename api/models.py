from rest_framework.exceptions import ValidationError
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length = 30, blank = False, null = False, unique = True)
    color = models.CharField(max_length = 10, blank = False, null = False)
    
    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length = 30, blank = False, null = False, unique = True)
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey('Category',on_delete = models.SET_DEFAULT, default = 1, null=False, blank = False)
    no_auth_needed = models.BooleanField(default = False)

    def __str__(self):
        return self.title


