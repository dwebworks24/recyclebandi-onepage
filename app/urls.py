
from django.urls import path
from .views import *
from .controler_logic import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('cluster_dashboard/', clusterdashboard, name='cluster_dashboard'),
    path('add_transaction/', cluster_form, name='add_transaction'),
    path('add_shop/', add_shop, name='add_shop'),
    # path('login/', login_logic, name='login'),
    path("logout/", logout_view, name="logout"),
    path("login/", mobial_otp_view, name="login"),
    path("verify_otp/", verified_otp_view, name="verify-otp"),

    path("auth/send_otp/", mobial_otp_logic, name="send_otp"),
    path("auth/verify_otp/", mobial_otp_verify_logic, name="verify-otp"),

    path("save_shop/", shop_owner_save_logic, name="save_shop"),
    
]
