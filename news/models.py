from django.db import models

class News(models.Model):
    headline = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    source = models.ForeignKey('outlet.Outlet', on_delete=models.CASCADE)
    link = models.URLField()