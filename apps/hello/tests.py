from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class BioViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('hello:index'))
        self.assertContains(response, "Name")
        self.assertContains(response, "Contacts")

