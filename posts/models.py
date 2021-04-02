from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='posts_image')

    def __str__(self):
        return self.title

