from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.cadastrar_aluno, name = 'cadastrar_aluno'),
    url(r'^register_multiples/$', views.RegistrosMultiplosViewSet.as_view(), name='set_registration_list'),
]
