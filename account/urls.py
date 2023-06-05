from django.urls import path
from .views import update_user_token, give_anon_token

urlpatterns = [
    path('test/update_access/', update_user_token),
    path("test/get_access/", give_anon_token),
]