from django.urls import path

from product import views

urlpatterns=[
    path('products/',views.product_list,name='product'),
    path('users/',views.user_list,name='users'),
    path('register/',views.register_user,name='register'),
    path('createproduct/',views.create_product,name='createproduct'),
    path('createorder/',views.create_order,name='createorder'),
    path('userorder/<user_id>',views.user_order_details,name='userorder'),
]