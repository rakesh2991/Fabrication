from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from ind import settings

admin.site.site_header = "SanrajEnterprises Admin"
admin.site.site_title = "SanrajEnterprises Portal"
admin.site.index_title = "Welcome to SanrajEnterprises"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')), 
               
    path('factory/', include('factory.urls')), 
    path('', RedirectView.as_view(url="factory/")),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)