from django.urls import path
from .views import HousesViewSet #HouseCreate
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

'''urlpatterns = [
    path('houses/create', HouseCreate.as_view(), name='house-create'),
]'''

router = SimpleRouter()

router.register('houses', HousesViewSet, 'houses')
#router.register('houses/create', HouseCreate, 'house-create')

#house_router = NestedSimpleRouter(router, "houses", lookup = 'house')

urlpatterns = router.urls
#urlpatterns += house_router.urls