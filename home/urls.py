from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginform, name='loginform'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logoutform, name='logoutform'),
    path('cart', views.cart, name='cart'),
    path('tracker/', views.tracker, name='tracker'),
    # path('orderNow/<int:cid>', views.orderNow, name='orderNow'),
    path('checkout', views.checkout, name='checkout'),
    path('product/<int:cid>', views.product_page, name='product_page'),
   
]
