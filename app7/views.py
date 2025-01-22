from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Cart, CartItem, Order, OrderProduct, Favourite
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request,'index.html')




@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, created_at__date=timezone.now())
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f'{product.name} was added to your cart.')
    return redirect('product_detail', product_id=product_id)

@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user, created_at__date=timezone.now()).first()
    if cart:
        items = CartItem.objects.filter(cart=cart)
    else:
        items = []
    
    return render(request, 'cart.html', {'cart': cart, 'items': items})

@login_required
def create_order(request):
    cart = Cart.objects.filter(user=request.user, created_at__date=timezone.now()).first()
    if not cart:
        messages.error(request, 'Your cart is empty.')
        return redirect('view_cart')

    order = Order.objects.create(user=request.user, created_at=timezone.now(), total=cart.total())
    for item in cart.items.all():
        OrderProduct.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)

    cart.delete()
    messages.success(request, 'Your order has been placed successfully.')
    return redirect('order_detail', order_id=order.id)

@login_required
def view_favourites(request):
    favourites = Favourite.objects.filter(user=request.user)
    return render(request, 'favourites.html', {'favourites': favourites})

@login_required
def add_to_favourites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favourite.objects.get_or_create(user=request.user, product=product)
    messages.success(request, f'{product.name} was added to your favourites.')
    return redirect('product_detail', product_id=product_id)

@login_required
def remove_from_favourites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favourite = Favourite.objects.filter(user=request.user, product=product).first()
    if favourite:
        favourite.delete()
        messages.success(request, f'{product.name} was removed from your favourites.')
    return redirect('view_favourites')



