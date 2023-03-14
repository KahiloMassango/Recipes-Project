from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):
    def test_recipe_category_views_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={'category_id': 1000
                        }
                    )
            )

        self.assertEqual(response.status_code, 404)

    def test_recipe_category_view_loads_correct_template(self):
        recipe = self.make_recipe(is_published=True)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': recipe.category.id}))  # noqa: E501
        self.assertTemplateUsed(response, 'recipes/pages/category.html')

    def test_recipe_category_template_loads_recipes(self):
        title_test = 'Category test'
        # Need a recipe for this test
        self.make_recipe(title=title_test)

    def test_recipe_category_template_dont_loads_unplubished_recipes(self):
        """Testing recipe is_published = False don't show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={'category_id': recipe.category.id
                        }
                )
        )

        self.assertEqual(response.status_code, 404)
