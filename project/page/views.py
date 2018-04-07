from django.shortcuts import render, get_object_or_404
from .models import Page

def index(request):
    return render(request, 'index.html')

def detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'default.html', {'page':page})
