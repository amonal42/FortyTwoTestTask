from django.test import TestCase

class AbsoluteUrlMainPageTests(TestCase):
    def test_index(self):
        response = self.client.get('')
        self.assertContains(response, "Bio")
        self.assertContains(response, "Contacts")
