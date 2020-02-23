from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny 

from components.helpers.custom_responses import CustomResponse

from components.helpers.random import randomString

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))

def login(request):
    response = CustomResponse()

   #email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')
   # password_verify = request.data.get('password_verify')

    # if email is None:
    #     return response.fieldError('email')
    if username is None:
        return response.fieldError('username')
    elif password is None:
        return response.fieldError('passowrd')
    # elif password_verify is None:
    #     return response.fieldError('passowrd_verify')
    
    # if password != password_verify:
    #     return response.error('Password does not match ')

    user = authenticate(username=username, password=password)
    if not user:
        return response.error('Invalid Credentials')
    Token.objects.filter(user=user).delete()
    token, created = Token.objects.get_or_create(user=user)

    body = {
        'username' : user.username,
        'email' : user.email,
        'token' : token.key

    }
    return response.data(body);

