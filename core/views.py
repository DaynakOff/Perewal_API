from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PerewalAddSerializer
from django.views.decorators.csrf import csrf_exempt


class SubmitDataAPIView(APIView):
    def post(self, request, format=None):
        serializer = PerewalAddSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            instance = serializer.save()
            response_data = {
                "status": 200,
                "message": None,
                "id": instance.id
            }
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            error_message = serializer.errors
            response_data = {
                "status": 400,
                "message": str(error_message)
            }
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
