from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name':'kahilo'
    })

def contato(request):
    pass

def sobre(request):
    pass