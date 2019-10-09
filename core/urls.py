from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('grupos.urls')),
    path('', include('turmas.urls')),
    path('', include('alunos.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_jwt_token),
]
