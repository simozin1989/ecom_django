from django.urls import path
from . import views
app_name = 'accounts'



urlpatterns = [
    path('singnup',views.signup , name='singnup' ),
    path('profile/<slug:slug>',views.profile , name='profile' ),

]