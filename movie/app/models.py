from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

# athourity of DB
class Authority(models.Model):
    scope = models.CharField(max_length=20)

# Depart of company
class Depart(models.Model):
    name = models.CharField(max_length=100)



# 지점
class BranchOffice(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20) # 서울, 경기
    def __str__(self):
        return self.name


class Sales(models.Model):
    branch_office = models.ForeignKey(BranchOffice, related_name='sales', on_delete=models.CASCADE)
    # 매출(어쩔 수 없는 하드코딩입니다.)
    jan_sales = models.FloatField()
    feb_sales = models.FloatField()
    mar_sales = models.FloatField()
    apr_sales = models.FloatField()
    may_sales = models.FloatField()
    jun_sales = models.FloatField()
    jul_sales = models.FloatField()
    aug_sales = models.FloatField()
    sep_sales = models.FloatField()
    oct_sales = models.FloatField()
    nov_sales = models.FloatField()
    dec_sales = models.FloatField()

# User model
class CustomUser(AbstractUser):
    rank = models.CharField(max_length=5)
    phone_number = models.TextField()

class CustomerUser(models.Model):
    user = models.ForeignKey(CustomUser, related_name='customer_user', on_delete=models.CASCADE)
    name = models.TextField()
    sex = models.TextField()
    birth_date = models.DateField()

class EmployeeUser(models.Model):
    user = models.ForeignKey(CustomUser, related_name='employee_user', on_delete=models.CASCADE)
    name = models.TextField()
    sex = models.TextField()
    birth_date = models.DateField()
    authority = models.ForeignKey(Authority, related_name="authority", on_delete=models.CASCADE)
    depart = models.ForeignKey(Depart, related_name="depart", on_delete=models.CASCADE)
    salary = models.TextField() # 나중에 정수형으로 바꿔줄 것.
    join = models.DateField() # 입사 날짜

# Movie model
class MovieInfo(models.Model):
    movie_id = models.CharField(max_length= 100, primary_key=True) # 영화이름
    movie_name = models.CharField(max_length=100)
    genre = models.TextField()
    director = models.TextField()
    movie_explanation = models.TextField()
    age_limit = models.CharField(max_length= 2)
    poster = models.ImageField()
    grade = models.FloatField(max_length= 2)

class TheaterInfo(models.Model):
    theater_name = models.CharField(max_length=50) # 상영관이름
    branch_office = models.ForeignKey(BranchOffice, related_name="theater_name", on_delete=models.CASCADE) #지점

class Seat(models.Model):
    theater_name = models.ForeignKey(TheaterInfo, related_name="seat", on_delete=models.CASCADE)
    seat_num = models.TextField()

class Screen(models.Model):
    movie_serial = models.CharField(max_length= 10, primary_key=True) # 같은 이름의 다른 영화
    movie_id = models.ForeignKey(MovieInfo, related_name="movie_info", on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    play_time = models.IntegerField()
    theater_number = models.ForeignKey(TheaterInfo, related_name="screen", on_delete=models.CASCADE)
    movie_price = models.IntegerField()
    kind = models.TextField() # 2D인지 3D인 지
    subtitle = models.BooleanField()

class Reservation(models.Model):
    customer = models.ForeignKey(CustomerUser, related_name="reservation_history", on_delete=models.CASCADE)
    #reservation_num = models.CharField(max_length=200, primary_key=True)
    movie_serial = models.ForeignKey(Screen, related_name="movie_reservation", on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, related_name="reservationer", on_delete=models.CASCADE)

