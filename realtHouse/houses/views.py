from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib.auth import get_user_model
from django.utils import timezone as tz


from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from django_filters import rest_framework as filters

from .models import Marketplace, HousePhoto, House
from account.models import AnonToken
from .serializers import HouseViewSetSerializer, HouseDetailSerializer
from .filters import HouseFilter


from redis.exceptions import DataError
from utils import redis_connect

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
class HousesViewSet(ReadOnlyModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseViewSetSerializer
    permission_classes = [AllowAny,]
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
        serializer = HouseDetailSerializer(house)
        return Response(serializer.data)
