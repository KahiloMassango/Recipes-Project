from django.db.models import Q
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404 
from utils.recipe.factory import make_recipe
from .models import Recipe
from .models import Category
# Create your views here.


def home(request):
    recipes =  Recipe.objects.filter(
        is_published=True
        ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
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

def recipe(request, id):
    recipe =  get_object_or_404(Recipe, id=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_datail_page': True,
    })

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404

    recipes = Recipe.objects.filter(
        Q(title__icontains=search_term) |
        Q(description__icontains=search_term)  
    ).order_by('-id')

    '''to make a queryset using OR operator use pipe "|" with Q. 
    or just use the way below
    recipes = Recipe.objects.filter(title__icontains=TERM_HERE) | Recipe.objects.filter(description__icontains=TERM_HERE)
    '''

    return render(request,'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': recipes
    })