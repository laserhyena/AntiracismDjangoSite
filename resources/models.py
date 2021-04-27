from django.db import models

# Create your models here.
class Resource(models.Model):
    CATEGORIES = [
        ("BK", "Book"),
        ("PC", "Podcast"),
        ("WS", "Workshop"),
    ]
    title = models.CharField(max_length=100)
    url = models.URLField()
    category = models.CharField(max_length=2, choices=CATEGORIES)
    # slug = models.SlugField()
    # body = models.TextField()
    # Don't think I need this..
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
