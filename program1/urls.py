"""
URL configuration for Tunç project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from customer.views import customer_list

urlpatterns = [
    path('customers/', customer_list, name='customer_list'),
]
from django.urls import path
from customer.views import customer_search

urlpatterns = [
    path('search/', customer_search, name='customer_search'),
]
from django.urls import path
from customer.views import customer_list, customer_delete, customer_create

urlpatterns = [
    path('customers/', customer_list, name='customer_list'),
    path('customers/<int:customer_id>/delete/', customer_delete, name='customer_delete'),
    path('customers/create/', customer_create, name='customer_create'),
]
