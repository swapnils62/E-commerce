from django.shortcuts import render, redirect
from home.models import Product
from .models import Cart, Cart_item
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def cart_create(request,id):
    product=Product.objects.get(id=id)

    cart=Cart.objects.filter(user=request.user).first()

    if not cart:
        cart=Cart.objects.create(user=request.user)
    
    cartitem=Cart_item.objects.filter(cart=cart,product=product).first()

    if cartitem:
        cartitem.quantity+=1
        cartitem.save()
    else:
        cartitem=Cart_item.objects.create(cart=cart,product=product,quantity=1)

    return redirect('/')

@login_required
def view_cart(request):
    cart=Cart.objects.filter(user=request.user).first()
    cartitem=Cart_item.objects.filter(cart=cart)
    total=0
    quantity=0
    for i in cartitem:
        total=(i.quantity*i.product.price)+total
        quantity=i.quantity+quantity
    return render(request,'html/cart.html',{'cartitem':cartitem,"total":total,"quantity":quantity})

@login_required
def delete_cartitem(request,id):
    cart=Cart.objects.get(user=request.user)
    cartitem=Cart_item.objects.get(cart=cart,id=id)
    cartitem.delete()
    return redirect('/cart')