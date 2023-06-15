from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib.auth import get_user_model
from django.utils import timezone as tz

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
#from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from django_filters import rest_framework as filters

from .models import Marketplace, HousePhoto, House
from account.models import AnonToken
from .serializers import HouseSerializer
from .filters import HouseFilter


from redis.exceptions import DataError
from utils import redis_connect, set_byn

redis_instance = redis_connect()

def test(request):
    return HttpResponse("Test")

def check_token(session_key):
    if redis_instance.get(name=session_key):
        result = True
    else:
        result = False
    
    return result
    


#TODO Pagination
class HousesViewSet(ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    #permission_classes = [AllowAny]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HouseFilter
    
    def get_queryset(self):
        try:
            #anon_token = AnonToken.objects.filter(token=self.request.session['anon-token']).first()
            #anon_token_check: bool = anon_token.exp_date>=tz.now()
            session_key = self.request.session.session_key
            anon_token_check = check_token(session_key)
        except KeyError:
            anon_token_check = False
        except DataError:
            self.request.session.create()
            session_key = self.request.session.session_key
            anon_token_check = check_token(session_key)
            
            
        try:
            user_access_check = ((self.request.user.is_authenticated) and (self.request.user.expiration_date > tz.now()))
        except AttributeError:
            user_access_check = False
            
        if user_access_check or anon_token_check:
            return self.queryset.all().order_by('-created_at')
        else:
            return self.queryset.filter(created_at__lt=tz.now()-tz.timedelta(hours=4)).all().order_by('-created_at')
        
        
    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        house = get_object_or_404(queryset, id=self.kwargs['pk'])
        serializer = HouseSerializer(house)
        return Response(serializer.data)

'''
{
    'amountusd': 200,
    'rent_rooms': 2,
    'address':"TestAddress",
    'description':awdadwawd,
    'marketplace_id':6,
    "user_id": 1,
    'location_a':12,
    'location_b'24:,
    'phoneNumber': "123123123",
    'photos':['test1', 'test2']
}
'''