from django.db import models
from django.urls import reverse


class Goods(models.Model):
    class STATUS(models.IntegerChoices):
        DRAFT = 0, "DRAFT"
        PUBLISHED = 1, "PUBLISHED"
    good = models.CharField(max_length=255, verbose_name="Товар")
    describe = models.TextField(blank=True, verbose_name="Опис")
    price = models.IntegerField(default=None, verbose_name="Ціна")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), STATUS.choices)), default=STATUS.PUBLISHED, verbose_name="Статус")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,related_name='cat' ,verbose_name="Категорії")
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')

    def __str__(self):
        return self.good

    def __repr__(self):
        return f"\n{self.good}\n{self.describe}"

    def get_absolute_url(self):
        return reverse("goodinfo", kwargs={"good_slug":self.slug})

    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товари"

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категорії")
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dcat", kwargs={"cat_slug":self.slug})
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class TagPost(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag_tag_slug_path", kwargs={"tag_slug":self.slug})