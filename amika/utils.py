from rest_framework_jwt.settings import api_settings

def jwt_payload_handler(user):
    return {
        'id_usuario': user.pk,
        'username': user.username,
        'nome': user.first_name,
        'sobrenome': user.last_name,
        'superusuario': user.is_superuser,
    }

def jwt_response_payload_handler(token, user=None, request=None):
    """ Custom response payload handler.
     This function controlls the custom payload after login or token refresh. This data is returned through the web API.
    """
    return {
        'token': token,
    }