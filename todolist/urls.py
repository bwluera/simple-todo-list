"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolistapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('create_task', views.create_task),
    path('delete_task/<int:id>', views.delete_task),
    path('update_task/<int:id>/<str:checked>', views.update_task),
    path('register', views.register),
    path('logout', views.logout_view),
    path('login', views.login_view)
]
