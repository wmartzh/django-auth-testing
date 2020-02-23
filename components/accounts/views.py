from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny 

from components.helpers.custom_responses import CustomResponse
from .serializer import UserSerializer
from components.helpers.random import randomString
from .models import User

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


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):

    response = CustomResponse()

    email = request.data.get('email')
    username = request.data.get('username')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    password = request.data.get('password')
    pass_verify =request.data.get('password_verify')

    valid_usrnm = User.objects.filter(username=username)
    valid_email = User.objects.filter(email=email)
    if email is None :
        return response.fieldError('email')
    elif username is None:
        return response.fieldError('password')
    elif password is None:
        return response.fieldError('password')
    elif pass_verify is None:
        return response.fieldError('password_verify')
    
    if password != pass_verify:
        return response.error('Password does not match ')

   

    if valid_usrnm.exists():
        return response.error(username+' is already taken')
    elif valid_email.exists():
        return response.error(email+' is already taken')



    user = User.objects.create_user(username=username,email=email,password=password)
    
    data = {
        'email':user.email,
        'username':user.username,
        'password' : user.password
    }
    return response.data(data=data)

