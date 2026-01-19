"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
from authantication.views import Signup_view,logout_view
from cart.views import cart_create,view_cart,delete_cartitem
from order.views import choose_add,New_address,Order_sum,place_order,Orderhistory
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('profile/', views.profile_view),
    path('about/', views.about_view),
    path('feedback/', views.feedback_view),
    path('Address/', views.add_address),
    path('updateadd/', views.update_address),
    path('signup/', Signup_view),
    path('out/', logout_view),
    path('additem/<int:id>/', cart_create),
    path('cart/', view_cart),
    path('product/<int:id>/', views.product_view),
    path('delete/<int:id>/', delete_cartitem),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chooseadd/', choose_add),
    path('newaddress/', New_address),
    path('newaddress/', New_address),
    path('ordersum/<int:id>/', Order_sum),
    path('orderplaced/<int:id>/', place_order),
    path('orderhistory/', Orderhistory),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)