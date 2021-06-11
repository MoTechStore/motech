from django.contrib import admin
from django.urls import path
from blog import views
from blog.views import RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('test/', views.test, name="test"),
    path('add_vehicle/',views.add_vehicle,name='add_vehicle'),
    path('savedata/', views.crud.savedata, name='savedata'),
    path('pay/', views.crud.pay, name='pay'),
    path('registerform/', views.registerform, name="registerform"),
    path('loginform/', views.loginform, name="loginform"),
    path('reg/', views.register, name="reg"),
    path('regi/', views.regi, name="regi"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='blog/index.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name="logout"),




]
