from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_jwt_token, name='login'),
    path('verificar-chave/', verify_jwt_token, name='verificar-chave'),
    path('', include('amika.urls'))
    path('', include('amika.urls')),
]
