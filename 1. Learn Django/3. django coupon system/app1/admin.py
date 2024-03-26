from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display =['academic_level', 'service_type', 'currency', 'price']


admin.site.register(Order, OrderAdmin)
