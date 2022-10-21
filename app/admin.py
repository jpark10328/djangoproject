from django.contrib import admin
from .models import Hotel, Room, Order, Comment

class HotelAdmin(admin.ModelAdmin):
    list_display = ('hname','owner')
    search_fields = ['hname']

class RoomAdmin(admin.ModelAdmin):
    list_display = ('roomnum',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('visit_at',)


admin.site.register(Hotel, HotelAdmin)

admin.site.register(Room, RoomAdmin)

admin.site.register(Order, OrderAdmin)

admin.site.register(Comment)