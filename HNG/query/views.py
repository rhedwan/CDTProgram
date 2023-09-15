from .serializers import (

    QueryParametersSerializer, UserSerializer
)
from .models import User
from rest_framework.views import APIView
import datetime
from rest_framework.response import Response
from rest_framework import renderers, status, generics


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"




class HNG(APIView):
    renderer_classes = [renderers.JSONRenderer]

    def get(self, request):
        # Deserialize and validate the query parameters
        serializer = QueryParametersSerializer(data=request.query_params)
        if serializer.is_valid():
            slack_name = serializer.validated_data["slack_name"]
            track = serializer.validated_data["track"]

            # You can now use slack_name and track in your logic
            # For example, you can return a response with these values
            now = datetime.datetime.utcnow()

            utc_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
            data = {
                "slack_name": slack_name,
                "current_day": datetime.datetime.now().strftime("%A"),
                "utc_time": utc_time,
                "track": track,
                "github_file_url": "https://github.com/rhedwan/CDTProgram/blob/main/HNG/query/views.py",
                "github_repo_url": "https://github.com/rhedwan/CDTProgram/tree/main/HNG",
                "status_code": 200,
            }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)