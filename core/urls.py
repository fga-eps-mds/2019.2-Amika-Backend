from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('grupos.urls')),
    path('', include('turmas.urls')),
    path('', include('alunos.urls')),
    path('', include('agendas.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_jwt_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)