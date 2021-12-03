from django.shortcuts import render

def index(request):
	return render(request, 'home/index.html')

def signin(request):
	return render(request, 'home/signin.html')

def signup(request):
	return render(request, 'home/signup.html')