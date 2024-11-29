from django.urls import path
from .views import *

urlpatterns=[
    path("chome",Customerview.as_view(),name="chome"),
    path("plist/<str:cat>",Productlistview.as_view(),name="plist"),
    path("pdetails/<int:pid>",Productdetailsview.as_view(),name="pdetails"),
    path("padd/<int:id>",Addtocart,name="padd"),
    path("cart",cartView.as_view(),name="cartlist"),
    path("incquantity/<int:id>",increaseQuantity,name="incquantity"),
    path("dec/<int:id>",DecreaseQuantity,name="decrsqnty"),
    path("deleteitem/<int:id>",Deleteitem,name="deleteitem"),
    path("placeorder/<int:id>",placeOrderView,name="placeorder"),
    path("orderlist",OrderView.as_view(),name="order"),
    path("cancel",cancelorder,name="ordercancel"),
    path('search',searchproduct,name="search")
]