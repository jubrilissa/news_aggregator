from django.db import models


class Outlet(models.Model):
    name = models.CharField(max_lenght=100)
    tagline = models.TextField(null=True)
    home_url = models.URLField(null=True)
