from django.urls import path
from .import views
# from app_main.views import Imageview
from django.conf import settings


urlpatterns = [
    # path('',views.home_main,name="home"),
    
    path('login',views.login_main,name="login"),
    path('register',views.register_main,name="register"),
    path('logout',views.logout_main,name="logout"),
    path('accounts',views.accounts_main,name="accounts"),
    path('enlarger',views.enlarger_main,name="enlarger"),
]
