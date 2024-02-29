from http.client import BAD_REQUEST, METHOD_NOT_ALLOWED, OK
from django.shortcuts import render ,HttpResponse
import requests
from .serializers import RouteSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import json
from rest_framework.exceptions import ParseError
from json.decoder import JSONDecodeError
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from rest_framework import status
from rest_framework import generics
from .models import  Route
from .serializers import  RouteSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

 
# Create your views here.


def index(request):
    return HttpResponse("Welcome to the Route app's Page!!")

@csrf_exempt
def main_route(request):
    if request.method == 'POST':
        try:
            route_data= JSONParser().parse(request)
            route_serializer=RouteSerializer(data=route_data)
            if route_serializer.is_valid():
                route_serializer.save()
                return HttpResponse("Booking is done successfully", status=OK)
            else:
                return JsonResponse(route_serializer.errors, status=BAD_REQUEST)
        except JSONDecodeError as e:
            return HttpResponse("Invalid JSON data", status=BAD_REQUEST)
    else:
        return HttpResponse("Only POST method is allowed", status=METHOD_NOT_ALLOWED)
    
class RouteListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'items_per_page'
    max_page_size = 100
    

class RouteListAPIView(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    pagination_class = RouteListPagination
    ordering_fields = ['route_id', 'route_name']  # Fields for sorting
    filter_backends = [filters.SearchFilter]
    search_fields = ['route_id', 'route_name', 'route_origin', 'route_destination']  # Fields for searching

class RouteDetailAPIView(generics.RetrieveAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    
