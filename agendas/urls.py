from django.urls import path
from agendas.views import enviar_anexo, listar_anexos

urlpatterns = [
    path('anexo', enviar_anexo, name='enviar_anexo'),
    path('anexos', listar_anexos, name='listar_anexos')
]
