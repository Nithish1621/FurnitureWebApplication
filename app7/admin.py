from django.contrib import admin
from .models import Product, Cart, CartItem, Order, OrderProduct, Favourite

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Favourite)



