from django.db import models


# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)