from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipe.factory import make_recipe
from .models import Recipe
from .models import Category
# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
        ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })

def recipe(request, id):
    recipe =  get_object_or_404(Recipe, id=id)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_datail_page': True,
    })

def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
        category_id=category_id, 
        is_published=True
        ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title':f'{recipes[0].category} - Category |'
    }) 
