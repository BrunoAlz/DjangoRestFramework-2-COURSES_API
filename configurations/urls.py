
from django.contrib import admin
from django.urls import path, include

from api.urls import router

urlpatterns = [
    path('', include('core.urls')),
    path('Contas/', include('accounts.urls')),
    path('api/v1/', include('api.urls')),
    path('api/v2/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]

