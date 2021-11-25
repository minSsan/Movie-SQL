from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main.html')

def movie_list(request):
    return render(request, 'movie-list.html')

def movie_detail(request):
    return render(request, 'movie-detail.html')

def ticketing(request):
    return render(request, 'ticketing.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def events(request):
    return render(request, 'events.html')

def forget(request):
    return render(request, 'forget.html')

def findID(request):
    return render(request, 'findID.html')