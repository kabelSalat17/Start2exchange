from django.contrib import admin
from .models import Order, Profile

admin.site.register([Order, Profile])
