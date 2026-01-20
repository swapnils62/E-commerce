from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cart.models import Cart,Cart_item
from home.models import Address
from home.forms import Add_address
from .models import Order, Orderitem
from home.models import Product
# Create your views here.

@login_required
def choose_add(request,productid=None):
    address=Address.objects.filter(user=request.user)
    return render(request, 'html/choose_address.html',{"address":address,"productid":productid})

@login_required
def New_address(request):
    if request.method == 'POST':
        form = Add_address(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user   
            address.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = Add_address()
    return render(request, 'html/address.html', {'form': form})

@login_required
def Order_sum(request,id,productid=None):
    
    if productid:
        product=Product.objects.get(id=productid)
        address=Address.objects.get(id=id,user=request.user)
        quantity=1
        total=product.price*quantity
        data={"product":product,'address':address,"total":total,"quantity":quantity}
    
    else:
        cart=Cart.objects.get(user=request.user)
        cartitem=Cart_item.objects.filter(cart=cart)
        address=Address.objects.get(id=id,user=request.user)

        total=0
        for i in cartitem:
            total=(i.quantity*i.product.price)+total
        
        data={"cart_items":cartitem, 'address':address,"total":total}
    return render(request, 'html/order_sum.html',data)

@login_required
def place_order(request,id,productid=None):

    if productid:
        product=Product.objects.get(id=productid)
        address=Address.objects.get(id=id,user=request.user)
        quantity=1
        total=product.price*quantity
        order=Order.objects.create(user=request.user,address=address,total_amount=total)

        Orderitem.objects.create(
            order=order,
            product=product,
            price=product.price,
            quantity=quantity,
            subtotal=product.price*quantity
        )
    else:
        address=Address.objects.get(id=id,user=request.user)
        cart=Cart.objects.get(user=request.user)
        cartitem=Cart_item.objects.filter(cart=cart)

        total=0
        for i in cartitem:
            total=(i.quantity*i.product.price)+total

        
        order=Order.objects.create(user=request.user,address=address,total_amount=total)

        for i in cartitem:
            Orderitem.objects.create(
                order=order,
                product=i.product,
                price=i.product.price,
                quantity=i.quantity,
                subtotal=i.product.price*i.quantity
            )
        
        cartitem.delete()
    return render(request, 'html/orderplace.html',)


def Orderhistory(request):
    order=Order.objects.filter(user=request.user)
    orderitem = Orderitem.objects.filter(order__in=order)
    return render(request, 'html/orderhistory.html',{"order":order,"orderitem":orderitem})
