from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self):
        self.recipe = self.make_recipe()