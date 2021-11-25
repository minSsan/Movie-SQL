from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#  class User(AbstractUser):
#      customer_rank = models.CharField(max_length= 1)
#      customer_phonenum = models.IntegerField()

# class Employer(AbstractUser):
#     employer_phonenum = models.IntegerField()
#     authority = models.CharField(max_length= 1)
#     department = models.TextField()
#     salary = models.CharField(max_length= 10)
#     branchoffice = models.TextField()
#     dateofjoin = models.CharField(max_length= 6)

class Movie_info(models.Model):
    movie_id = models.CharField(max_length= 10)
    movie_name = models.TextField()
    genre = models.TextField()
    director = models.TextField()
    movie_explanation = models.TextField()
    age_limit = models.CharField(max_length= 2)
    poster = models.ImageField()
    grade = models.FloatField(max_length= 2)

class Screen_info(models.Model):
    movie_serial = models.CharField(max_length= 10)
    movie_id = models.CharField(max_length= 10)
    playtime = models.IntegerField()
    theaternumber = models.CharField(max_length= 3)
    movie_price = models.IntegerField()

class Screen(models.Model):
    movie_id = models.CharField(max_length = 10)
    kind = models.TextField()
    subtitle = models.BooleanField()

class Customer_Pesonal_info(models.Model):
    customer_phonenum = models.IntegerField()
    customer_name = models.TextField()
    customer_sex = models.TextField()
    customer_birthdate = models.IntegerField()

class Reservation(models.Model):
    reservation_num = models.CharField(max_length= 10)
    movie_serial = models.CharField(max_length= 10)
    seat = models.CharField(max_length= 4)

class Employer_Personal_info(models.Model):
    employer_phonenum = models.IntegerField()
    employer_name = models.TextField()
    employer_sex = models.TextField()
    employer_birthdate = models.IntegerField()

