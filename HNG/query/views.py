from .serializers import (

    QueryParametersSerializer,
)
from rest_framework.views import APIView
import datetime

class HNG(APIView):
    def get(self, request):
        # Deserialize and validate the query parameters
        serializer = QueryParametersSerializer(data=request.query_params)
        if serializer.is_valid():
            slack_name = serializer.validated_data["slack_name"]
            track = serializer.validated_data["track"]

            # You can now use slack_name and track in your logic
            # For example, you can return a response with these values
            data = {
                "slack_name": slack_name,
                "current_day": datetime.datetime.now().strftime("%A"),
                "utc_time": datetime.datetime.utcnow(),
                "track": track,
                "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
                "github_repo_url": "https://github.com/rhedwan/repo",
                "status_code": 200,
            }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)