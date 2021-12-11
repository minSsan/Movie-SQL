from django import forms
from django.contrib import admin

from .models import *

# Register your models here.

# User admin
admin.site.register(CustomUser),
admin.site.register(CustomerUser),
admin.site.register(EmployeeUser),

# Movie admin
admin.site.register(MovieInfo),
admin.site.register(Screen),
admin.site.register(TheaterInfo),
admin.site.register(Reservation),
admin.site.register(Seat),

# branch admin
admin.site.register(BranchOffice),
admin.site.register(Sales),

# employee specific admin
admin.site.register(Depart),
admin.site.register(Authority),