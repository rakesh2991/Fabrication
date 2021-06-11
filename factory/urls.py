from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from factory import views
# ------------restframe work------------
# from rest_framework import routers
# 
# router = routers.DefaultRouter()
# router.register(r'product', views.ProductViewSet)
# router.register(r'service', views.ServiceViewSet)
# router.register(r'news', views.NewsViewSet)

urlpatterns = [ 
    path('home/', views.HomeView.as_view()),
    path('about/', views.AboutView.as_view()),
#     
    path('service/', views.ServiceListView.as_view()),    
    path('service/<int:pk>', views.ServiceDetailView.as_view()), 
    
    path('product/', views.ProductListView.as_view()),    
    path('product/<int:pk>', views.ProductDetailView.as_view()),    
# 
    path('news/', views.NewsListView.as_view()),    
    path('news/<int:pk>', views.NewsDetailView.as_view()),    

    path('vender/create/', views.VenderCreate.as_view(success_url="/factory/home")),
#     
    path('contact/submit', views.contact),
# 
    path('contact/', views.ContactView.as_view()),
    
    path('', RedirectView.as_view(url="home/")),   
    
#     admin permision ke liya 
    path('service/create/', views.ServiceCreate.as_view(success_url="/factory/service")),
    path('service/delete/<int:pk>', views.ServiceDeleteView.as_view(success_url="/factory/service")),
    
    path('product/create/', views.ProductCreate.as_view(success_url="/factory/product")),
    path('product/delete/<int:pk>', views.ProductDeleteView.as_view(success_url="/factory/product")),
#   rest api link
#     path(r'api/', include(router.urls)),  
]
