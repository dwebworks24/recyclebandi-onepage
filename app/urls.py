
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_transaction/', cluster_form, name='add_transaction'),
    path('add_shop/', add_shop, name='add_shop'),
    path('login/', login_logic, name='login'),
    path("logout/", logout_view, name="logout"),
]
