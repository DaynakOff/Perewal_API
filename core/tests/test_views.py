import pytest
from rest_framework.test import APIClient
from core.models import Users, Coords, Level, PerewalAdd


@pytest.fixture()
def api_client():
	return APIClient()


@pytest.fixture()
def setup_objects():
	user = Users.objects.create(email='test1@test.com', family='Test1', name='Test2', otc='Test3', phone='+79876543210')
	coords = Coords.objects.create(longitude=200.0, latitude=200.0, height=200.0)
	level = Level.objects.create(summer='A', winter='B', autumn='C', spring='D')
	perewal = PerewalAdd.objects.create(
		beauty_title='Горный перевал',
		title='Перевал Дятлова',
		other_title='',
		connect='',
		add_time='2023-01-01T12:00:00Z',
		status='new',
		coords=coords,
		user=user,
		level=level
	)
	return perewal


@pytest.mark.django_db
def test_perewa_list(api_client, setup_objects):
	response = api_client.get('/api/pereval/')
	assert response.status_code == 200
	assert len(response.data) > 0


@pytest.mark.django_db
def test_perewa_detail(api_client, setup_objects):
	perewal = setup_objects
	response = api_client.get(f'/api/pereval/{perewal.id}/')
	assert response.status_code == 200
	assert 'beauty_title' in response.json()
