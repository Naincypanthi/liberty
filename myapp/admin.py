from django.contrib import admin
from django.utils.html import format_html
from .models import products
from .models import user
from .models import order

class productAdmin(admin.ModelAdmin):
    list_display=["name","price","category","types","brand","image"]

class userAdmin(admin.ModelAdmin):
    list_display=["firstname","lastname","email","password"]
class orderAdmin(admin.ModelAdmin):
    list_display=["name","email","password","color","size","pin","phone_no","address","pay_mode","products","city"]

admin.site.register(products,productAdmin)
admin.site.register(user,userAdmin)
admin.site.register(order,orderAdmin)

# Register your models here.
