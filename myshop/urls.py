from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.products_list, name='products_list'),
    path('categories/', views.categories_list, name='categories_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('cart/', views.cart, name='cart'),
    path('order/<int:product_id>/', views.order_create, name='order_create'),
    path('order/success/', views.order_success, name='order_success'),
]
