from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,TemplateView,DetailView
from account.models import Products,Cart,Order
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"please login first")
            return redirect("log")
    return inner

decorators=[never_cache,signin_required]

@method_decorator(decorator=decorators,name="dispatch")
class Customerview(TemplateView):
    template_name="chome.html"

@method_decorator(decorator=decorators,name="dispatch")    
class Productlistview(ListView):
    template_name="productlist.html"
    queryset=Products.objects.all()
    context_object_name="products"
    def get_queryset(self) :
        cat=self.kwargs.get("cat")
        self.request.session["category"]=cat
        return self.queryset.filter(category=cat)

def searchproduct(request,*args,**kwargs):
    keyword=request.POST["searchkey"]
    cat=request.session["category"]
    if keyword:
        products=Products.objects.filter(title__icontains=keyword,category=cat)
        return render(request,"productlist.html",{"products":products})
    else:
        messages.warning(request,"invalid search keyword")
        return redirect("plist",cat=cat)


@method_decorator(decorator=decorators,name="dispatch")    
class Productdetailsview(DetailView):
    template_name="productdetails.html"
    queryset=Products.objects.all()
    context_object_name="product"
    pk_url_kwarg="pid"



decorators
def Addtocart(request,**kwargs):
    try:
        pid=kwargs.get("id")
        products=Products.objects.get(id=pid)
        user=request.user
        cartcheck=Cart.objects.filter(products=products,user=user).exists()
        if cartcheck:
            cartitem=Cart.objects.get(products=products,user=user)
            cartitem.quantity+=1
            cartitem.save()
            messages.success(request,"quantity increased")
            return redirect("chome")
        else:
            Cart.objects.create(products=products,user=user)
            messages.success(request,"succesffully addedd to cart")
            return redirect("chome")
    except Exception as e:
        print(e)
        messages.warning(request,"sometingwent wrong")
        return redirect("chome")
    
@method_decorator(decorator=decorators,name="dispatch")
class cartView(ListView):
    template_name="cart.html"
    queryset=Cart.objects.all()
    context_object_name='product'
    def get_queryset(self):
        qs=self.queryset.filter(user=self.request.user)
        return qs

decorators
def increaseQuantity(request,*args,**kwargs):
    try:
        cid=kwargs.get("id")
        cart=Cart.objects.get(id=id)
        cart.quality+=1
        cart.save()
        return redirect("cartlist")
    except:
        messages.warning(request,"something wrong")
        return redirect("cartlist")
decorators
def DecreaseQuantity(request,args,*kwargs):
    try:
        cid=kwargs.get('id')
        cart=Cart.objects.get(id=cid)
        if cart.quality==1:
            cart.delete()
            return redirect('cartlist')
        else:
            cart.quality-=1
            cart.save()

            return redirect('cartlist')
    except:
        messages.warning(request,"Something Went Wrong!!")
        return redirect('cartlist')
decorators
def Deleteitem(request,*args,**kwargs):
    try:
        cid=kwargs.get('id')   
        cart=Cart.objects.get(id=cid)
        cart.delete()
        messages.success(request,'Item Removed From Cart!')
        return redirect('cartlist')
    except:
        messages.warning(request,"Something Went Wrong!!")
        return redirect('cartlist')
decorators    
def placeOrderView(request,**kwargs):
    try:
        cid=kwargs.get("id")
        cart=Cart.objects.get(id=cid)
        Order.objects.create(product=cart.products,user=request.user,quantity=cart.quality)
        cart.delete()

        #mailsending
        subject="egadgets Order Notification"
        msg=f"order for {cart.products.title} is placed"
        f_rom="sufiyanakpa@gmail.com"
        to_id=request.user.email
        send_mail(subject,msg,f_rom,[to_id])

        messages.success(request,f'{cart.products.title}\'s order placed')
        return redirect("cartlist")
    except Exception as e:
        print (e)
        messages.warning(request,"something went wrong")
        return redirect("cartlist")

@method_decorator(decorator=decorators,name="dispatch")    
class OrderView(ListView):
    template_name="orders.html"
    queryset=Order.objects.all()
    context_object_name="orders"
    def get_queryset(self) :
        return Order.objects.filter(user=self.request.user)
 

decorators 
def cancelorder(request,**kwargs):
    try:
        oid=kwargs.get("id")
        order=Order.objects.get(id=oid)
        order.status="Cancelled"
        order.save()
        
        messages.success(request,"order Cancelled")
        return redirect("orders")
    except Exception as e:
        print(e)
        messages.warning(request,"something wrong")
        return redirect("order")
    






