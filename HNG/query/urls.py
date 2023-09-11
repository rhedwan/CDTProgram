from django.urls import path
from .views import  HNG

urlpatterns = [
    path("hng/", HNG.as_view(), name="profile"),
]