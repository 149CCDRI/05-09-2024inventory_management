from django.contrib import admin
from django.urls import path, include
from . import views
from user import views as user_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.service_list, name='service_list'),
    path('clients/', views.clients, name='clients'),
    path('suppliers/', views.suppliers, name='suppliers'), 
    path('materials/', views.materials, name='materials'),
    path('orders/', views.place_order, name='place_order'),
    path('order_success/', views.order_success, name='order_success'),
    path('inventory/', views.inventory, name='inventory'),
    path('admin/', admin.site.urls),
    path('register/', user_view.register, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='template/user/login.html'), name='user.login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='template/user/logout.html'), name='user.logout'),
    # Add more URLs for other functionalities
]

