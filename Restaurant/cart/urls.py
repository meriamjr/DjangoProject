from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('browsing/', views.product_list, name='product_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart,
name='remove_from_cart'),
    path('addqty/<int:product_id>/', views.add_qty, name='add_qty'),
    path('subqty/<int:product_id>/', views.sub_qty, name='sub_qty'),
]