from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import DataManager


class SubmitDataAPIView(APIView):
    def post(self, request):
        data = request.data
        data_manager = DataManager()
        data_manager.save_perewal(data)

        try:
            result = data_manager.save_perewal(request.data)
            return Response({'message': 'Данные успешно сохранены', 'id': result}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': 'Ошибка при сохранении данных'}, status=status.HTTP_400_BAD_REQUEST)
