from wsgiref.util import request_uri

from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status, generics
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


class PerewalDetailView(generics.RetrieveAPIView):
	queryset = PerewalAdd.objects.all()
	serializer_class = PerewalAddSerializer
	lookup_field = 'id'

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		return Response(
			{
				'status': 200,
				'data': serializer.data,
			}
		)


class PerewalUpdateView(generics.UpdateAPIView):
	queryset = PerewalAdd.objects.all()
	serializer_class = PerewalAddSerializer
	lookup_field = 'id'

	def update(self, request, *args, **kwargs):
		partial = kwargs.pop('partial', False)
		instance = self.get_object()

		if instance.status != 'new':
			return Response(
				{
					"state": 0,
					"message": 'Нельзя редактировать объект в не статутса new'
				},
				status=status.HTTP_400_BAD_REQUEST
			)

		incoming_data = request.data.copy()
		protected_fields = ['family', 'name', 'otc', 'email', 'phone']
		for field in protected_fields:
			if field in incoming_data:
				del incoming_data[field]

		serializer = self.get_serializer(instance, data=incoming_data, partial=partial)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)

		return Response(
			{
				"state": 1,
				"message": 'Объект успешно обновлен'
			},
			status=status.HTTP_200_OK
		)


class PerewalsByUserView(generics.ListAPIView):
	serializer_class = PerewalAddSerializer

	def get_queryset(self):
		email = self.request.query_params.get('user__email')
		if email is not None:
			return PerewalAdd.objects.filter(user__email=email)
		return []
