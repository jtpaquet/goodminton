from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('product/', views.product, name="product"),
    path('home/', views.home, name="home"),
    path('update_item/', views.updateItem, name="update_item"),
]