from django.http import HttpResponse
from django.shortcuts import render
from .models import Settings


def home(request):
    context = dict()
    context['settings'] = Settings.objects.first()
    return render(request, 'index.html', context)
