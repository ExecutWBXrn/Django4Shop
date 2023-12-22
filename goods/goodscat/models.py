from django.db import models

class Goods(models.Model):
    good = models.CharField(max_length=255)
    describe = models.TextField(blank=True)
    price = models.IntegerField(default=None)
    is_published = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
