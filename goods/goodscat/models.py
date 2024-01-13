from django.db import models
from django.urls import reverse


class Goods(models.Model):
    good = models.CharField(max_length=255)
    describe = models.TextField(blank=True)
    price = models.IntegerField(default=None)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    is_published = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.good

    def __repr__(self):
        return f"\n{self.good}\n{self.describe}"

    def get_absolute_url(self):
        return reverse("goodinfo", kwargs={"good_slug":self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.name