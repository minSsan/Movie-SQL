# for Ajax
import json

from django.core import serializers
from django.db.models.query import QuerySet
from django.http import JsonResponse

# for user
from django.contrib import auth, messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# for query
## filter(Q(속성이름__icontains = 검색물))로 이용
from django.db.models import Q

from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone


from .models import BranchOffice, CustomUser, CustomerUser, EmployeeUser, MovieInfo, Sales, Screen, Seat, TheaterInfo, Reservation


import datetime


# Create your views here.
def home(request):
    print(request.user)
    return render(request, 'main.html')

def movie_list(request):
    return render(request, 'movie-list.html')

def movie_detail(request):
    return render(request, 'movie-detail.html')

def ticket_list(request):
    if request.user:
        movies = MovieInfo.objects.all()
        context = {
            'movies' : movies,
            }
        return render(request, 'ticketing.html', context)
    else:
        return redirect('login')


def ticketing(request):
    context = {}
    branch_names = []
    if request.is_ajax:
        if request.GET.get('message') == "movie_name_click":
            res_id = request.GET.get('movie_id')
            ticket_date = request.GET.get('ticket_date')
            if not ticket_date:
                context = {
                    'alert':"날짜를 먼저 선택해주세요.",
                }
                return JsonResponse(context, status=200)
            #movies = MovieInfo.objects.filter(movie_id = res_id)
            #print("선택된 영화:", movies)
            screens = Screen.objects.filter(movie_id = res_id)
            screens = screens.filter(start_time__date=ticket_date)
            #print("선택된 영화 상영 정보:", screens)
            theaters = []
            for screen in screens:
                theaters.append(((screen.theater_number).branch_office).city)
            context = {
                'theaters': list(set(theaters)),
            }
            #print("선택된 영화가 상영되는 지점 정보:", context)
            return JsonResponse(context, status=200)
        
        elif request.GET.get('message') == "theater_city_click":
            res_id = request.GET.get('movie_id')
            ticket_date = request.GET.get('ticket_date')
            branch_offices = BranchOffice.objects.filter(city=request.GET.get('movie_city'))
            print("branch_offices: ", branch_offices)
            
            theaters = TheaterInfo.objects.all()
            theaters = theaters.filter(branch_office__in=branch_offices)
            # print("theaters: ", theaters)
           
            screens = Screen.objects.filter(start_time__date=ticket_date)
            screens = screens.filter(movie_id=res_id, theater_number__in=theaters)
            #print("screens: ", screens)
            
            branch_names = []
            for screen in screens:
                branch_names.append(((screen.theater_number).branch_office).name)
            context = {
                'branch_names': list(set(branch_names)),
            }
            return JsonResponse(context, status=200)

        elif request.GET.get('message') == "theater_branch_click":
            movie_id = request.GET.get('movie_id')
            theater_city = request.GET.get('theater_city')
            branch_name = request.GET.get('branch_name')
            ticket_date = request.GET.get('ticket_date')
            branch_office = BranchOffice.objects.get(name=branch_name, city=theater_city)
            print("branch_office: ", branch_office)
            theaters = TheaterInfo.objects.all()
            theaters = theaters.filter(branch_office=branch_office)
            print("theaters: ", theaters)
            screens = Screen.objects.filter(start_time__date=ticket_date)
            print("screens: ", screens)
            screens = screens.filter(theater_number__in=theaters, movie_id=movie_id)
            
            print("screens",screens)

            screen_list = []
            for screen in screens:
                screen_list.append({
                    'theater_name': screen.theater_number.theater_name,
                    'start_time': screen.start_time,
                    'end_time': screen.end_time,
                })

            context = {
                'screens': screen_list,
            }

            return JsonResponse(context, status=200)
        elif request.POST['message'] == 'submit':
            branch_name = request.POST['branch_name']
            # print("branch_name:", branch_name)
            theater_city = request.POST['theater_city']
            # print("theater_city:", theater_city)
            theater_name = request.POST['theater_name']
            # print("theater_name:", theater_name)
            movie_id = request.POST['movie_id']
            # print("movie_id:", movie_id)
            start_time = request.POST['start_time']
            # print("start_time:", start_time)

            branch_office = BranchOffice.objects.get(name=branch_name, city=theater_city)
            # print("branch_office: ",branch_office)
            theater = TheaterInfo.objects.get(theater_name=theater_name, branch_office=branch_office)
            print("theater: ", theater)
            screen = Screen.objects.get(movie_id=movie_id, start_time=start_time,theater_number=theater)
            print("screen: ", screen)
            all_seats = Seat.objects.filter(theater_name=theater)
            print("all_seats: ", all_seats)
            reservations = Reservation.objects.filter(movie_serial=screen, seat__in=all_seats)
            
            seat_context = {
                'all_seats': list(all_seats.values()),
                'reservations': list(reservations.values()),
                'seat_rows': int(len(list(all_seats.values())) / 18) + 1,
            }
            
            return JsonResponse(seat_context, status=200)

        elif request.POST['message'] == 'reservation':
            seat_num = request.POST['seat_num']
            branch_name = request.POST['branch_name']
            # print("branch_name:", branch_name)
            branch_city = request.POST['branch_city']
            # print("theater_city:", theater_city)
            theater_name = request.POST['theater_name']
            # print("theater_name:", theater_name)
            movie_id = request.POST['movie_id']
            # print("movie_id:", movie_id)
            start_time = request.POST['start_time']
            # print("start_time:", start_time)

            branch_office = BranchOffice.objects.get(name=branch_name, city=branch_city)
            # print("branch_office: ",branch_office)
            theater = TheaterInfo.objects.get(theater_name=theater_name, branch_office=branch_office)
            # print("theater: ", theater)
            movie_serial = Screen.objects.get(movie_id=movie_id, start_time=start_time,theater_number=theater)
            seat = Seat.objects.get(theater_name=theater, seat_num=seat_num)

            # customer, movie_serial, seat 으로 새로운 Reservation 생성
            reservation = Reservation()
            print("user", CustomerUser.objects.get(user=request.user));
            reservation.customer = CustomerUser.objects.get(user=request.user)
            reservation.movie_serial = movie_serial
            reservation.seat = seat
            reservation.save()

            return JsonResponse({
                   'success': True,
                   'url': reverse('reservationinfo')
                })
            
            if (reservation.save()): 
                return JsonResponse({
                   'success': True,
                   'url': reverse('mypage')
                })
            else:
                return JsonResponse({'success': False})
            

    # if request.method == "POST":
        # 영화이름 movie
        # 극장 theater
        # 날짜
        # 시간
        # 좌석
        # 유저
        # A이면~~ B이면 ~~ 해서 짤라서 보내줌
    #return HttpResponse("hi")
    return JsonResponse(context, status=200)

def ticketing_seat(request, context):
    return render(request, 'ticketing_seat.html', context)

def events(request):
    return render(request, 'events.html')

def event_detail(request):
    return render(request, 'event_detail.html')

def forget(request):
    return render(request, 'forget.html')

def findID(request):
    return render(request, 'findID.html')

def signup_view(request):

    # POST 방식으로 요청이 들어올 경우.
    if request.method == "POST":

        # 패스워드가 같은지 체크
        if request.POST['password1'] == request.POST['password2']:
            # 회원가입
            custom_user = CustomUser()
            custom_user.username = request.POST['username']
            custom_user.password = request.POST['password1']
            custom_user.phone_number = request.POST['phone_number']
            custom_user.rank = '1'
            custom_user.save()
            customer_user = CustomerUser()
            customer_user.user = custom_user
            customer_user.sex = request.POST['sex']
            customer_user.birth_date = request.POST['birth_date']


            # 회원가입과 동시에 로그인도 해주는 기능
            user = authenticate(request=request, username=custom_user.username, password=custom_user.password)
            ##login(request=request, user=user)
            return redirect("home")
        
        # 패스워드가 다른 경우
        else:
            return HttpResponse("패스워드가 일치하지 않습니다.")
        
    # GET 방식으로 요청이 들어올 경우.
    else:
        context = {

        }
        return render(request, 'signup.html', context)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username='admin', password='1234')
        if user is not None:
            print('로그인')
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "유저의 형식이 옳지 않습니다.")
            print("유저의 형식이 옳지 않습니다.")
            return redirect("home")
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("home")

def mypage(request):
    user_query = CustomUser.objects.get(username=request.user)
    if CustomerUser.objects.filter(user=user_query):
        print('일반유저')
        return render(request, './mypage/mypage.html')
    elif EmployeeUser.objects.filter(user=user_query):
        print('관리자유저')
        return render(request, './manage_page/manage_main.html')
    return redirect('login')

def events(request):
    return render(request, 'events.html')

def eventrecord(request):
    return render(request, './mypage/eventrecord.html')

def infomodification(request):
    return render(request, './mypage/infomodification.html')

def reservationinfo(request):
    user = CustomerUser.objects.get(user=request.user)
    reservations = Reservation.objects.filter(customer=user)
    context = dict()
    context['reservations'] = []
    for reservation in reservations:
        date = reservation.movie_serial.start_time
        reservation_info = {
            'movie_name': reservation.movie_serial.movie_id.movie_name,
            'branch_city': reservation.seat.theater_name.branch_office.city,
            'branch_name': reservation.seat.theater_name.branch_office.name,
            'theater_name': (reservation.seat.theater_name).theater_name,
            'seat': reservation.seat.seat_num,
            'start_time': str(date.year)+"."+str(date.month)+"."+str(date.day)+" / "+str(date.hour)+":"+str(date.minute),
            'play_time': reservation.movie_serial.play_time,
        }
        context['reservations'].append(reservation_info)
    # print(context)
    return render(request, './mypage/reservationinfo.html', context) 


def manage_main(request):
    return render(request, './manage_page/manage_main.html')

def manage_revenue(request):
    branch_office = BranchOffice.objects.all()
    context = {
        'branch_office' : branch_office,
    }

    return render(request, './manage_page/manage_revenue.html', context)

# Ajax 통신
def manage_revenue_search(request):

    data = request.GET.get('data')
    branch_col = BranchOffice.objects.get(name=data)
    sales_data_set = Sales.objects.filter(branch_office=branch_col)
    sales_data_list = []
    for sales_data in sales_data_set:
        sales_data_list.append(sales_data.jan_sales)
        sales_data_list.append(sales_data.feb_sales)
        sales_data_list.append(sales_data.mar_sales)
        sales_data_list.append(sales_data.apr_sales)
        sales_data_list.append(sales_data.may_sales)
        sales_data_list.append(sales_data.jun_sales)
        sales_data_list.append(sales_data.jul_sales)
        sales_data_list.append(sales_data.aug_sales)
        sales_data_list.append(sales_data.sep_sales)
        sales_data_list.append(sales_data.oct_sales)
        sales_data_list.append(sales_data.nov_sales)
        sales_data_list.append(sales_data.dec_sales)
    print(sales_data_list)
    context = {
        'sales' : sales_data_list
    }
    return JsonResponse(context, status=200)

