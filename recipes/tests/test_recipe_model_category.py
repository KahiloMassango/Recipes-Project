from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self):
        self.category = self.make_category(name='Category testing')
        return super().setUp()

    def test_recipe_category_model_string_representation_is_name_field(self):
        self.assertEqual(str(self.category),  self.category.name)

    def test_recipe_category_model_name_field_max_length_is_64_chars(self):
        category = self.make_category('A' * 70)
        with self.assertRaises(ValidationError):
            category.full_clean()
