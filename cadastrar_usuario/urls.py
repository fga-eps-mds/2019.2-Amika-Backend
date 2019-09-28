from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.cadastrar_aluno, name = 'cadastrar_aluno'),
    path('register_multiples/', views.MultipleRegistrationsViewSet.as_view(), name='set_registration_list'),
]