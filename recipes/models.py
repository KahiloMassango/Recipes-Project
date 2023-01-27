from django.contrib.auth.models import User
from django.db import models
from django import forms


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Recipe(models.Model):

    Prep_unit_choices = (
        ('MINUTE', 'Minute/s'),
        ('HOUR', 'Hour/s'),)

    Servings_unit_choices = (
        ('PLATES','Plate/s'),
        ('PEOPLE','People/s'),
    )
    # title description slug
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    # preparation_time preparation_time_unit
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=10, choices=Prep_unit_choices, default="MINUTE")
    # servings servings_unit
    servings = models.IntegerField()
    serving_unit = models.CharField(max_length=10,  choices=Servings_unit_choices, default="PLATES")
    # preparation_step
    preparation_steps = models.TextField()
    # preparation_step_is_html
    preparation_step_is_html = models.BooleanField(default=False)
    # created_at updated_at
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # is_published
    is_published = models.BooleanField(default=False)
    # cover
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    # category (Relação)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null =True, blank=True, default=None)
    # Author (Relação)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title