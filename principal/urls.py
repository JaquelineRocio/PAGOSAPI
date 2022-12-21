
from django.contrib import admin
from django.urls import re_path,path, include
from versionedPagos.v1.router import api_urlpatterns as api_v1
from versionedPagos.v2.router import api_urlpatterns as api_v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pagos.urls')),

    path('users/', include('users.urls')),
    re_path(r'^api/v1/', include(api_v1)),
    re_path(r'^api/v2/', include(api_v2)),
]