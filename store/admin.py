from django.contrib import admin
from .models import Product,Cart,CartItem,Order,OrderItem
# Register your models here.

admin.site.register(Product)

class CartItemInline(admin.TabularInline):
    model = CartItem
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]