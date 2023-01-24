from django.urls import path
from recipes.views import home, sobre, contato


urlpatterns = [
    path('', home, name='home'), # Home
    path('sobre/', sobre, name='sobre'), #  /sobre/
    path('contato/', contato, name='contato'), # /contato/
]
