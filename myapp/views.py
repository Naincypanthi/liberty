from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import products
from .models import user
from .models import order as xyz
from .cart import Cart
def home(request):
    x=products.objects.all()
    data={
        "info":x
    }
    return render(request,"home.html",data)


def home2(request,category):
    print(category)
    x=products.objects.filter(category=category)[0:3]
    data={
        "info":x
    }
    return render(request,"home.html",data)
def shop(request,category):
    
    x=products.objects.filter(category=category)
    data={
        "info":x
    }
    return render(request,"shop.html",data)

def addToCart(request):
    name=request.POST['name']
    price=request.POST['price']
    qty=request.POST['qty']
    image=request.POST['image']
    ob=Cart(name,price,image,qty)
    print(ob.showProduct())
    if "cart" in request.session:
        # request.session['cart'].append([ob.name,ob.price,ob.qty,ob.image])
        temp=request.session['cart']
        temp.append([ob.name,ob.price,ob.qty,ob.image])
        request.session['cart']=temp
    else:
        temp=[[ob.name,ob.price,ob.qty,ob.image],]
        request.session['cart']=temp
    return redirect(home)

def displayCart(request):
    xyz=request.session["cart"]
    t=0
    for item in xyz:
        t=t+int(item[1])

    print("total ",t)        
        
    
         
    data={
        "info":xyz,
        "total":t,
    }
    return render(request,"displayCart.html",data)

    
       

def clearCart(request):
    if "cart" in request.session:
        request.session.pop("cart")
    return redirect(home)
def delete(request):
    index=int(request.POST['index'])
    temp=request.session['cart']
    temp.pop(index)
    request.session['cart']=temp
    data={
        'info':request.session['cart']
    }
    return redirect(displayCart)
def page(request,id):
    info=products.objects.get(id=id)
    data={
        "info":info
    }
    return render(request,"page.html",data)


def registration(request):
    if(request.method=="POST"):
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        ob=user(firstname=firstname,lastname=lastname,email=email,password=password)
        ob.save()
        data={
            "msg":"Account Created..."
        }
        return render(request,"account.html",data)
        
    else:
        return render(request,"account.html")
def login(request):
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['password']
        ob=user.objects.filter(email=email,password=password).exists()
        if(ob==True):
            temp=user.objects.get(email=email,password=password)
            request.session['users']=[temp.firstname,temp.lastname,temp.email,temp.password]
            return redirect(dashboard)
        else:
            return redirect(invalid)
    return render(request,"login.html")
def dashboard(request):
    if("users" in request.session):
        return redirect(order)
        # return render(request,"dashboard.html",data)
    else:
        return redirect(login)
def invalid(request):
    return render(request,"invalid.html")
def logout(request):
    request.session.pop("users")
    return redirect(login)
def order(request):
    if "users" in request.session:
        if(request.method=="POST"):
            name=request.POST["name"]
            email=request.POST["email"]
            size=request.POST["size"]
            color=request.POST["color"]
            pin=request.POST["pin"]
            address=request.POST["address"]
            pay_mode=request.POST["pay_mode"]
            products=request.session['cart']
            city=request.POST["city"]
            phone_no=request.POST["phone_no"]
            ob=xyz(name=name,email=email,size=size,color=color,pin=pin,address=address,pay_mode=pay_mode,city=city,phone_no=phone_no,products=products)
            ob.save()
            request.session.pop("users")
            request.session.pop("cart")
            return redirect(home    )
        else:
            return render(request,"order.html")
    else:
        return redirect(login)
        







    
# Create your views here.
