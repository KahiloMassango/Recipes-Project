from django.shortcuts import render
from django.http import HttpResponse
from utils.recipe.factory import make_recipe
from .models import Recipe

# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
        ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })

def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_datail_page': True,
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category_id=category_id, 
        is_published=True
        ).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes
    }) 
