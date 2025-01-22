from django.urls import path
from . import views

urlpatterns = [
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('order/create/', views.create_order, name='create_order'),
    path('favourites/', views.view_favourites, name='view_favourites'),
    path('favourites/add/<int:product_id>/', views.add_to_favourites, name='add_to_favourites'),
    path('favourites/remove/<int:product_id>/', views.remove_from_favourites, name='remove_from_favourites'),
]
