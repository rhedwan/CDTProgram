from django.urls import path
from .views import  HNG

urlpatterns = [
    path("api/", HNG.as_view(), name="profile"),
]