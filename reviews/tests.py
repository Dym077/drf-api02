from django.test import TestCase

# Create your tests here
from reviews.models import Review

class TestReviewForm(TestCase):

    def test_form_is_valid(self):
        review_form = Review({'content': 'This is a great post'})
        self.assertTrue(review_form.is_valid())
