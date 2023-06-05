from django.urls import path
from .views import HousesViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter


router = SimpleRouter()

router.register('houses', HousesViewSet, 'houses')

#house_router = NestedSimpleRouter(router, "houses", lookup = 'house')

urlpatterns = router.urls
#urlpatterns += house_router.urls