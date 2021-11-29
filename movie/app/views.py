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

def event_detail(request):
    return render(request, 'event_detail.html')

def forget(request):
    return render(request, 'forget.html')

def findID(request):
    return render(request, 'findID.html')

def mypage(request):
    return render(request, './mypage/mypage.html')

def eventrecord(request):
    return render(request, './mypage/eventrecord.html')

def infomodification(request):
    return render(request, './mypage/infomodification.html')

def reservationinfo(request):
    return render(request, './mypage/reservationinfo.html')  