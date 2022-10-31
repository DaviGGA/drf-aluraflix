from django.db import models

class Video(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
