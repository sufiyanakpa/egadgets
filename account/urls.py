from django.urls import path
from .views import *

urlpatterns=[
    path("log",LoginView.as_view(),name="log"),
    path("reg",RegView.as_view(),name="reg"),
    path("logout",Logoutview.as_view(),name="logout")
]