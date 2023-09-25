from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # APP URLS
    path('account/', include('account.api.urls')),
    # API URLS
    path('api/v1/', include('grocery.api.urls')),
    path('api/v1/account/', include('account.api.urls')),
]
