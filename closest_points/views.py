from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Point
import itertools


@csrf_exempt
def closest_points(request):
    if request.method == 'POST':
        coordinates = request.POST.get('points', '')
        points = coordinates.split(';')
        point_objects = []
        
        # Calculate closest points
        closest_points = []
        min_distance = float('inf')
        for pair in itertools.combinations(points, 2):
            point1 = tuple(map(int, pair[0].split(',')))
            point2 = tuple(map(int, pair[1].split(',')))
            distance = ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
            if distance < min_distance:
                closest_points = [point1, point2]
                min_distance = distance
    
        point = Point(coordinates=coordinates, closest_points=';'.join([','.join(map(str, p)) for p in closest_points]))
        point.save()

        return JsonResponse({'closest_points': closest_points})
    else:
        return JsonResponse({'error': 'Invalid method.'})

