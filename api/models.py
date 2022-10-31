from rest_framework.exceptions import ValidationError
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    url = models.URLField()

    def save(self,*args,**kwargs):
        if Video.objects.filter(title = self.title):
            raise ValidationError(f"The video '{self.title}' alrealdy exist")
        else:
            return super().save(*args,**kwargs)

    def __str__(self):
        return self.title
