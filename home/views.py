from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from home.models import Order, Product, Tracker
from django.http import JsonResponse
import json

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home/home.html', context)
def loginform(request):
    if request.method == "POST":
        login_username = request.POST['login-username']
        login_password = request.POST['login-password']

        user = authenticate(username = login_username, password = login_password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("unable to login")
    return render(request, 'home/login.html')
def signup(request):
    if request.method == "POST":
        fullname = request.POST['register-name']
        username = request.POST['register-username']
        email = request.POST['register-email']
        password = request.POST['register-password']
        
        if len(username) < 10 or len(password) < 10:
            messages.error(request, "This is not a correct order")
            return HttpResponse("Unable to Signup. Username must be greater than 10 character and password also")
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fullname
            myuser.save()
    return render(request, 'home/register.html')

def logoutform(request):
    logout(request)
    return redirect('loginform')
def cart(request):
    return render(request, 'home/cart.html')
def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('orderEmail', '')
        try:
            order = Order.objects.filter(order_id = orderId, email = email)
            if len(order) > 0:
                update = Tracker.objects.filter(order_id = orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.description, 'timestamp': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("else")
        except Exception as e:
            return HttpResponse("exception")
    return render(request, 'home/tracker.html')

# def orderNow(request, cid):
#     products= Product.objects.filter(pk =  cid).first()
#     context = {
#         'product': products
#     }
#     return render(request, 'home/cart.html', context)
def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST['itemsJson']
        firstname = request.POST['firstname']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        state= request.POST['state']
        zip = request.POST['zip']
        cardname = request.POST['cardname']
        cardnumber= request.POST['cardnumber']
        cvv = request.POST['cvv']

        order = Order(item_json = itemsJson, name = firstname, email = email, address = address, city = city, state = state, zip = zip, card_number= cardnumber, card_holder = cardname, cvv = cvv)
        order.save()
        update = Tracker(order_id = order.order_id, description = "Your order has been approved successfully")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'home/checkout.html', {'thank' : thank, 'id' : id})
    return render(request, 'home/checkout.html')



def product_page(request, cid):
    product = Product.objects.filter(pk = cid).first()
    context = {
        'product':product
    }
    return render(request, 'home/product_page.html', context)

