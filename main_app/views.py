from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def cat_index(request):
  cats = Cat.objects.all()
  # [{"name": "c1", "breed":"breed1"}, {"name":"c2", "breed":"breed2"}, {}]
  return render(request, 'cats/index.html', {'cats': cats})

def cat_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  print(cat)
  return render(request, 'cats/detail.html', { 'cat': cat })