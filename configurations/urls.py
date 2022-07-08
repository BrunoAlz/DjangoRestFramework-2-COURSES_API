
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('Contas/', include('accounts.urls')),
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]

