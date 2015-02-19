from django.db import models

# Create your models here.


class PersonInfo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=100, blank=True)
    jabber = models.CharField(max_length=100, blank=True)
    skype = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    other_contacts = models.TextField(blank=True)

    def __str__(self):
	return " ".join((self.first_name, self.last_name))
