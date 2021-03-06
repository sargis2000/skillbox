from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shops.models import Product, MarketModel
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from app_users.models import Profile


@login_required(login_url='/accounts/login/')
@require_POST
def cart_add(request, product_id, magazine_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    magazine = get_object_or_404(MarketModel, id=magazine_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(magazine=magazine,
                 product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


@login_required(login_url='/accounts/login/')
def cart_remove(request, product_id, magazine_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    market = get_object_or_404(MarketModel, id=magazine_id)
    cart.remove(product, market)
    return redirect('cart_detail')


@login_required(login_url='/accounts/login/')
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart, 'balance': Profile.objects.get(user=request.user).balance})