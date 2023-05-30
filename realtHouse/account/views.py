from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.conf import settings 

import redis

import random
import string

from .models import AnonToken

from redis.exceptions import DataError
from utils import redis_connect

redis_instance = redis_connect()

def generate_random_string() -> str:
    token = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(20))
    return token

def update_user_token(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = get_user_model().objects.get(id=user_id)
        user.update_access()
        return HttpResponse('Update Token Successfully')
    else:
        try:
            request.session['anon-token']
            return HttpResponse(f"No auth, but you have maybe access {request.session['anon-token']}")
        except KeyError:
            return HttpResponse(f"No token - no auth")    
        

def give_anon_token(request):
    #anon_token = AnonToken.objects.create_token() #Тут в редиске заносим анон_кей
    anon_token = generate_random_string()
    
    session_key = request.session.session_key
    if session_key == None:
        session_key = request.session.create()
        
    session_key = request.session.session_key
    redis_instance.set(name=session_key, value=anon_token, ex=300)
    
    request.session['anon-token'] = anon_token
    #print(request.session['anon-token'])
    #return HttpResponse(f"Set anon-token successfully: {request.session['anon-token']}")
    #return HttpResponse(
    #    f"Test request: {session_key}, anon_token: {redis_instance.get(name=session_key)}")
    return HttpResponseRedirect('/houses/')
    redirrect
