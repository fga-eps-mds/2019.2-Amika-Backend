from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.tela_de_cadastro, name = 'tela_de_cadastro'),
    url(r'^register_multiples/$', views.RegistrationViewSet.as_view(), name='teste'),
]