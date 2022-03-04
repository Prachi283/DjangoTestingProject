from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=60)
    seo_title = models.CharField(max_length=59)
    seo_description = models.CharField(max_length=160)
    abstract = models.CharField(max_length=160)
    body = models.TextField(default="")
    duration = models.IntegerField(default=0)
    slug = models.SlugField(max_length=20)
    start_date = models.DateTimeField()
    price = models.IntegerField()
    location = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"