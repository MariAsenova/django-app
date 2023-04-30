from django.contrib import admin

# Register your models here.

from .models import Coffee, CoffeeType, Size

admin.site.register(Coffee)
admin.site.register(CoffeeType)
admin.site.register(Size)

