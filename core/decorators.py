from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

def autentica_administrador(view):
    @csrf_exempt
    def wrapper(request, *args, **kwargs):
        try:
            token = {'token': request.headers['Authorization']}
            valid = VerifyJSONWebTokenSerializer().validate(token)
            user = User.objects.get(username=valid['user'])
            if user.is_superuser:
                return view(request, *args, **kwargs)
            else:
                return JsonResponse({'error': 'Acesso permitido somente ao administrador'}, status=403)
        except:
            return JsonResponse({'error': 'Logue no sistema'}, status=403)
    return wrapper  

def autentica_aluno(view):
    @csrf_exempt
    def wrapper(request, *args, **kwargs):
        try:
            token = {'token': request.headers['Authorization']}
            valid = VerifyJSONWebTokenSerializer().validate(token)
            user = User.objects.get(username=valid['user'])
            return view(request, *args, **kwargs)
        except:
            return JsonResponse({'error': 'Logue no sistema'}, status=403)
    return wrapper
