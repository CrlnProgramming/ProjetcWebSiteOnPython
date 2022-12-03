from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'base/home.html')

def word(request):
	return render(request, 'base/word.html')
