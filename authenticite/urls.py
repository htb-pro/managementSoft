from django.urls import path
from authenticite.views import *

urlpatterns=[
    path('auth',Authentification_User,name="login"),
    path('deconnection',Deconnection_user,name="logout"),
    path('index',index,name="index")
]