from django.urls import path
from .views import  HNG, UserRetrieveUpdateDestroy, UserListCreate

urlpatterns = [
    path("api/task_one/", HNG.as_view(), name="profile"),
    path("api/<int:id>", UserRetrieveUpdateDestroy.as_view(), name="user_retrieve_update"),
    path("api/", UserListCreate.as_view(), name="user"),
]