from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('product/detail/<pk>', product_detail, name='product-detail'),
    path('search/', product_search, name='search'),
    path('category/product/<pk>',category_filtering, name='category-filter'),
    path('add-to-cart/<pk>',add_to_cart, name='add_to_cart'),
    path('add-inc/<pk>',inc_cart, name='inc-cart'),
    path('add-dec/<pk>',dec_cart, name='dec-cart'),
    path('cart_remove/<pk>',cart_remove, name='cart_remove'),
    path('cart-summary',cart_summary, name='cart-summary'),
    path('order-summary',order_summary, name='order-summary'),
    path('order-details/<pk>/',order_details, name='order-details'),
    path('add-wishlist/<pk>', add_to_wishlist, name='add-wishlist'),
    path('wishlist-product/', wishlist_product, name='wishlist_product'),


]