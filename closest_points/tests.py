from django.test import TestCase, Client
from django.urls import reverse
from .models import Point


class ClosestPointsAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_closest_points_api(self):
        url = reverse('closest_points')
        data = {'points': '2,2;-1,30;20,11;4,5'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['closest_points']), 2)

    def test_point_model(self):
        point = Point.objects.create(coordinates='2,2;-1,30;20,11;4,5', closest_points='2,2;4,5')
        self.assertEqual(point.coordinates, '2,2;-1,30;20,11;4,5')
        self.assertEqual(point.closest_points, '2,2;4,5')
