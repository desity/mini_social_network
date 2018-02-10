from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from requests import Response
from rest_framework.utils import json
from .clearbit import  *
from .emailhunter import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

import jwt,json
from rest_framework import views
from rest_framework.response import Response


def validateemail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def newuser(email, user, password, firstname, lastname):
#def newuser(**kwargs):
    result = ''
    clearbit = clearbit_def(email)
    if User.objects.filter(email=email).exists():
        result = 'The user with such email is already registered in this system'
    elif User.objects.filter(username=user).exists():
        result = 'The user with such username is already registered in this system'
    elif not validateemail(email) or verify_email(email):
        result = 'Please, input valid email'
    elif clearbit != 'None' and clearbit != (firstname+' '+lastname):
        result = 'You entered wrong Name/Surname. Your name is: ' + clearbit
    else:
        #User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        User.objects.create_user(email=email,
             username=user,
             password=password,
             first_name=firstname,
             last_name=lastname,
             is_active=True).save()
        result = user
    print(result)
    return result


#def log_in(username, password):

"""
    def log_in(username, password):
        try:
            user = User.objects.get(username=username, password=password, is_active=True)
        except User.DoesNotExist:
            return Response({'Error': "Invalid username/password"}, status="400")
        if user:
            payload = {
                'id': user.id,
                'email': user.email,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
            return HttpResponse(
                json.dumps(jwt_token),
                status=200,
                content_type="application/json"
            )
        else:
            return Response(
                json.dumps({'Error': "Invalid credentials"}),
                status=400,
                content_type="application/json"
            )
            
   payload = {
            "sub": "login",
            "user_id": User.objects.filter(login=login, password=password, active=True)[0].pk,
            "exp": time.mktime(settings.JWT_EXPIRE.timetuple()),
            "active": False
        }
        jwt_token = {'token': jwt.encode(payload, settings.SECRET_KEY)}
        result = jwt_token
    elif User.objects.filter(login=login, password=password).count() != 0:
        result = 'Please, activate your account via your e-mail'
    elif User.objects.filter(login=login, password=password).count() == 0:
        result = 'Username and Password do not mach'
    return result


def authorizate(token):
    try:
        payload = jwt.decode(token[:-2][12:], settings.SECRET_KEY)
        userid = payload['user_id']
        return userid
    except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
        return 'Error 403'

"""