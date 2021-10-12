from django.urls import path

from django.urls.conf import include

from product import views
app_name = 'product'



urlpatterns = [
    path('products', views.product_list),
    path('<slug:slug>',views.product_detail,name='product_detail'),

]