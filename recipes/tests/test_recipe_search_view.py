from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase

class RecipeSearchViewTest(RecipeTestBase):    
    def test_recipe_search_view_function_is_correct(self):
        url = reverse('recipes:search')
        resolved = resolve(url) 
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_view_loads_correct_template(self):
        url = reverse('recipes:search')
        response = self.client.get(url + '?q=test')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipes_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search' ) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_scaped(self):
        url = reverse('recipes:search')
        response = self.client.get(url + '?q=test')
        self.assertIn(
            'Search for &quot;test&quot;',
            response.content.decode('utf-8')
         )