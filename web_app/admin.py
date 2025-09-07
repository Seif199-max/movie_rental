from django.contrib import admin
from .models import Movies,Returns,Rentals
# Register your models here.
admin.site.register(Movies)
admin.site.register(Returns)
admin.site.register(Rentals)