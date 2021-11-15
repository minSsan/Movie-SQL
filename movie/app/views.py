from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main.html')

def movie_detail(request):
    return render(request, 'movie-detail.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')