from django.shortcuts import render
import models

# Create your views here.


def index(request):
    return render(request, 'hello/index.html',
                  {"info" : models.PersonInfo.objects.all()[0]})
