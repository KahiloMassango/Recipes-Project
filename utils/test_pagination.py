from django.urls import reverse
from recipes.tests.test_recipe_base import RecipeTestBase
from utils.pagination import make_pagination_range

class PaginationTest(RecipeTestBase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range = list(range(1, 21)),
            qtd_pages=4,
            current_page =1,
        )['pagination']
        self.assertEqual([ 1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa: E501
        # Current page = 1 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # Current page = 2 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # Current page = 3 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=3,
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)

        # Current page = 4 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=4,
        )['pagination']
        self.assertEqual([3, 4, 5, 6], pagination)

    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range = list(range(1, 21)),
            qtd_pages=4,
            current_page =1,
        )['pagination']
        self.assertEqual([ 1, 2, 3, 4], pagination)

    def test_make_sure_middle_ranges_are_correct(self):  # noqa: E501
        # Current page = 10 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=10,
        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)

        # Current page = 12 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=12 ,
        )['pagination']
        self.assertEqual([11, 12, 13, 14], pagination)
 
    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        # Current page = 18 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=18,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # Current page = 19 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=19,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # Current page = 20 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=20,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

    def test_pagination_shows_correct_qty_items_per_page(self):
        for i in range(0, 10):
            kwargs = {'slug':f'test{i}', 'title':f'title{i}', 'author_data':{'username': f'user{i}'}}
            self.make_recipe(**kwargs)



        response = self.client.get(reverse('recipes:home'))

        response_content = response.content.decode('utf-8')
        self.assertNotIn('title10', response_content)
        self.assertIn('title9', response_content)
        self.assertIn('title8', response_content)
        self.assertIn('title7', response_content)
        self.assertIn('title6', response_content)
        self.assertIn('title5', response_content)
        self.assertIn('title4', response_content)
        self.assertIn('title3', response_content)
        self.assertIn('title2', response_content)
        self.assertIn('title1', response_content)

        
       

