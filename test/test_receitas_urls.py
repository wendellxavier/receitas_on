from django.test import TestCase
from django.urls import reverse

class ReceitaURLsTest(TestCase):
    
    def test_receita_search_url_is_correct(self):
        url = reverse('receitas:search')
        self.assertEqual(url, '/receitas/search/')