from django.urls import path, include
from formulario_felicidade_autentica import views

urlpatterns = [
    path('form_felicidade/', views.gerencia_formulario_felicidade, name = 'form_a'),
]

