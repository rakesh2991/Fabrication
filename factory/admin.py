from django.contrib import admin
from factory.models import Category, Product, News, Service, Vender
from django.contrib.admin.options import ModelAdmin

admin.site.register(Category)

class ProductAdmin(ModelAdmin):
    list_display = ["name", "e_date"]
    search_fields = ["name", "description"]
    list_filter = ["e_date", "event_type"]
admin.site.register(Product, ProductAdmin)


class NewsAdmin(ModelAdmin):
    list_display = ["subject", "n_date"]
    search_fields = ["subject",  "description"]
    list_filter = ["n_date"]
admin.site.register(News, NewsAdmin)

class ServiceAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "description"]
    
admin.site.register(Service, ServiceAdmin)

class VenderAdmin(ModelAdmin):
    list_display = ["name", "phone_no"]
    search_fields = ["name", "description", "address"]
    list_filter = ["category"]
admin.site.register(Vender, VenderAdmin)



