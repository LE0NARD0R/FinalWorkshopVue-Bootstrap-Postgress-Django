from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from carddeck.models import Places
from carddeck.serializers import PlacesSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def PlacesApi(request, id=0):
    if request.method == 'GET':
        places = Places.objects.all()
        places_serializer = PlacesSerializer(places, many = True)
        return JsonResponse(places_serializer.data, safe = False)
    elif request.method == 'POST':
        places_data = JSONParser().parse(request)
        places_serializer = PlacesSerializer(data=places_data)
        if places_serializer.is_valid():
            places_serializer.save()
            return JsonResponse('Added succesfully', safe = False)
        return JsonResponse('Failed to add', safe = False)
    elif request.method == 'PUT':
        places_data = JSONParser().parse(request)
        places = Places.objects.get(PlaceID = places_data['PlaceID'])
        places_serializer = PlacesSerializer(places, data = places_data)
        if places_serializer.is_valid():
            places_serializer.save()
            return JsonResponse('Updated succesfully', safe = False)
        return JsonResponse('Failed to Update', safe = False)
    elif request.method == 'DELETE':
        places = Places.objects.get(PlaceID = id)
        places.delete()
        return JsonResponse('Deleted succesfully', safe = False)
    
@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)