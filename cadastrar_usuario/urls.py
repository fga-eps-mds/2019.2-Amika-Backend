from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.tela_de_cadastro, name = 'tela_de_cadastro'),
    url(r'^set_registration_list/$', views.set_registration_list, name="set_registration_list"),
    url(r'^teste/$', views.RegistrationViewSet.as_view(), name='teste'),
]