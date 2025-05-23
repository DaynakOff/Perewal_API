from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *

class UsersViewSet(ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = UsersSerializer


class CoordsViewSet(ModelViewSet):
	queryset = Coords.objects.all()
	serializer_class = CoordsSerializer


class LevelViewSet(ModelViewSet):
	queryset = Level.objects.all()
	serializer_class = LevelSerializer


class ImageViewSet(ModelViewSet):
	queryset = Image.objects.all()
	serializer_class = ImageSerializer


class PerewalAddViewSet(ModelViewSet):
	queryset = PerewalAdd.objects.all()
	serializer_class = PerewalAddSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		try:
			if not serializer.is_valid(raise_exception=True):
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			serializer.save()
			return Response(
				{
					'status': 200,
					'message': None,
					'id': serializer.instance.id
				},
				status=status.HTTP_200_OK
			)
		except DatabaseError as e:
			return Response(
				{
					'status': 500, 'message': 'Ошибка базы данных', 'id': None
				},
				status=status.HTTP_500_INTERNAL_SERVER_ERROR
			)




