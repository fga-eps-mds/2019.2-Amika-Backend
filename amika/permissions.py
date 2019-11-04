from rest_framework import permissions

import amika
from amika.models import *


class Permissoes(permissions.BasePermission):
    def has_permission(self, request, view):
        method = "{}_{}".format(request.method.lower(), request.path.split('/')[1].title().lower())

        return getattr(amika.permissions, method, usuario_eh_admin)(request)


def pk(request):
    return {'pk': dict(request.__dict__)['parser_context']['kwargs']['pk']}


# Usuários
def usuario_eh_admin(request):
    return request.user and request.user.is_staff


def usuario_autenticado(request):
    return request.user and request.user.is_authenticated


def usuario_eh_o_aluno(request):
    return request.user and \
           Aluno.objects.filter(**pk(request)) and \
           request.user.username == Aluno.objects.filter(**pk(request)).first().username


def usuario_participa_do_grupo(request):
    return request.user and \
           Grupo.objects.filter(**pk(request)).first().aluno_set.filter(username=request.user.username)


# Permissões
def post_aluno(request):
    return True


def get_aluno(request):
    return usuario_eh_o_aluno(request) or \
           usuario_eh_admin(request)


def put_aluno(request):
    return usuario_eh_o_aluno(request) or \
           usuario_eh_admin(request)


def get_grupo(request):
    return usuario_participa_do_grupo(request) or \
           usuario_eh_admin(request)


def get_agendas(request):
    return usuario_autenticado(request)


def get_agenda(request):
    return usuario_autenticado(request)


def get_materiais(request):
    return usuario_autenticado(request)


def get_material(request):
    return usuario_autenticado(request)
