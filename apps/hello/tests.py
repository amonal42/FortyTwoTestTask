from django.test import TestCase
from django.core.urlresolvers import reverse
from models import PersonInfo

# Create your tests here.
class MainPageViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('hello:index'))
        self.assertContains(response, "Bio")
        self.assertContains(response, "Contacts")

    def test_index_view_show_stored_person_name(self):
        pi = PersonInfo.objects.all()[0]
        pi.name = "Alex"
        pi.save()
        response = self.client.get(reverse('hello:index'))
        self.assertContains(response, "Alex")
