from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token, name='login'),
    path('verificar-chave/', verify_jwt_token, name='verificar-chave'),
    path('', include('amika.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
