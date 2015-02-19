from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class MainPageViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('hello:index'))
        self.assertContains(response, "Bio")
        self.assertContains(response, "Contacts")

