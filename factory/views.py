from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from factory.models import Service, Product, News, Vender
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, CreateView, DeleteView
# Category,  
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
# -----------rest framework-----------
# from rest_framework import viewsets
# from factory.myserializer import Productserializers, Serviceserializers, Newsserializers
# # , Userserializers
# from django.contrib.auth.models import User

def contact(req):
    sub = "factory Contact :: %s " % req.POST.get("uname")
    body = "Phone No = %s\nEMail = %s\nMessage = %s " % (req.POST.get("phone_no"), req.POST.get("email"),  req.POST.get("msg"))
    send_mail(
        sub,
        body,
        req.POST.get("email"),
        ['project.modules123@gmail.com'],
        fail_silently=False,
    )
    return HttpResponseRedirect("/factory/home?msg=Submited Successfully")

class HomeView(TemplateView):
    template_name = "factory/home.html"

class AboutView(TemplateView):
    template_name = "factory/about.html"
 
class ContactView(TemplateView):
    template_name = "factory/contact.html"
# 
class ServiceListView(ListView):
    model = Service
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return Service.objects.filter(Q(name__icontains = si)).order_by("-id")[:12]

class ServiceDetailView(DetailView):
    model = Service
    
class ProductListView(ListView):
    model = Product
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return Product.objects.filter(Q(name__icontains = si) | Q(description__icontains = si) | Q(event_type__name__icontains = si)).order_by("-id")[:12]
 
class ProductDetailView(DetailView):
    model = Product
 
class NewsListView(ListView):    
    model = News
    def get_queryset(self):
        return News.objects.order_by("-id")[:10]
 
class NewsDetailView(DetailView):
    model = News
         
class VenderCreate(CreateView):
    model = Vender
#     fields = ["name", "phone_no", "email", "description", "address", "category"]
    fields = "__all__"
#     def form_valid(self, form):
#         self.object = form.save()
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())
# #     --------i have a use a code multi option feild-------------
# class VenderCreate(CreateView):
#     model = Vender
#     fields = ["name", "phone_no", "email", "description", "address", "category"]
#     def form_valid(self, form):
#         self.object = form.save()
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name="dispatch")    
class ServiceCreate(CreateView):
    model = Service
    fields = "__all__"
    
    
@method_decorator(login_required, name="dispatch")    
class ServiceDeleteView(DeleteView):
    model = Service
    
@method_decorator(login_required, name="dispatch")    
class ProductCreate(CreateView):
    model = Product
    fields = "__all__"
    
@method_decorator(login_required, name="dispatch")    
class ProductDeleteView(DeleteView):
    model = Product
#     
# --------------Restframe work set----------------
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all().order_by('-id')
#     serializer_class = Productserializers
#     def get_queryset(self):
#         si = self.request.GET.get("si")
#         if si == None:
#             si = ""
#         return Product.objects.filter(Q(name__icontains = si) | Q(description__icontains = si) | Q(event_type__name__icontains = si)).order_by("-id")[:12]
# 
# class ServiceViewSet(viewsets.ModelViewSet):
#     queryset = Service.objects.all().order_by('-id')
#     serializer_class = Serviceserializers
#     def get_queryset(self):
#         si = self.request.GET.get("si")
#         if si == None:
#             si = ""
#         return Service.objects.filter(Q(name__icontains = si)).order_by("-id")[:12]
#     
# class NewsViewSet(viewsets.ModelViewSet):
#     queryset = News.objects.all().order_by('-id')
#     serializer_class = Newsserializers
#     def get_queryset(self):
#         return News.objects.order_by("-id")[:10]

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-id')
#     serializer_class = Userserializers    
#     
    
    
    
    
    
    
    