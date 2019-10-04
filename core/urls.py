from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('turmas.urls')),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^login/', obtain_jwt_token),
]
