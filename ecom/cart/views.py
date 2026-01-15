from django.shortcuts import render, redirect
from home.models import Product
from .models import Cart, Cart_item
# Create your views here.
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

    return redirect('/home')

def view_cart(request):
    cart=Cart.objects.filter(user=request.user).first()
    cartitem=Cart_item.objects.filter(cart=cart)
    return render(request,'html/cart.html',{'cartitem':cartitem})

def delete_cartitem(request,id):
    cart=Cart.objects.get(user=request.user)
    cartitem=Cart_item.objects.get(cart=cart,id=id)
    cartitem.delete()
    return redirect('/cart')