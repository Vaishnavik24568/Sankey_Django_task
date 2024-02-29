import genericpath
from http.client import BAD_REQUEST, METHOD_NOT_ALLOWED, OK
from warnings import filters
from django.shortcuts import render ,HttpResponse
from .models import Trip
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django.http import JsonResponse
from .serializers import TripSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import json
from rest_framework.exceptions import ParseError
from json.decoder import JSONDecodeError
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from rest_framework import status
import requests
from django.http import JsonResponse
# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework import filters

class CustomPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size' 
    max_page_size = 1000  

class TripListAPIView(ListAPIView):
    queryset = Trip.objects.all()     # trip list all with the trip list view 
    serializer_class = TripSerializer
    pagination_class = CustomPagination
    ordering_fields = ['trip_id', 'user_id']  # Fields for sorting
    filter_backends = [filters.SearchFilter]
    search_fields = ['trip_id','user_id', 'driver_name'] 
    


class TripDetailAPIView(APIView):
    def get(self, request, trip_id):
        try:
            trip = Trip.objects.get(trip_id=trip_id)
            serializer = TripSerializer(trip)
            return JsonResponse(serializer.data)  
        except Trip.DoesNotExist:
            return JsonResponse({'error': 'Trip not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Internal Server Error. Error: {str(e)}'}, status=500)
        
    def retrieve(self, request, *args, **kwargs):
        trip_instance = self.get_object()
        trip_data = TripSerializer(trip_instance).data

        # Fetch associated booking details from Booking service using interservice call
        booking_details = self.fetch_booking_details(trip_data.get('trip_id'))

        # Combine trip details with booking details
        combined_data = {**trip_data, 'booking_details': booking_details}

        return JsonResponse(combined_data)

    def fetch_booking_details(self, trip_id):
        # Interservice call to Booking service
        booking_url = f'http://booking/bookings/?trip_id={trip_id}'

        try:
            booking_response = requests.get(booking_url)

            if booking_response.status_code // 100 == 2:
                booking_data = booking_response.json()
                return booking_data
            else:
                # Handle non-successful response
                return {'error': 'Failed to fetch booking details'}

        except requests.RequestException as e:
            # Handle exception, for example, log the error
            return {'error': 'Internal server error during interservice call to Booking service'}
    
def index(request):
    return HttpResponse("Trip pages ...........")

@csrf_exempt
def create_trip(request):
    if request.method == 'POST':
        try:
            trip_data = JSONParser().parse(request)
            trip_serializer = TripSerializer(data=trip_data)
            if trip_serializer.is_valid():
                trip_serializer.save()  
                return JsonResponse("Booking is successful")
            else:
                return JsonResponse(trip_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError as e:
            return JsonResponse({'message': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)
        except ParseError as e:
            return JsonResponse({'message': 'Invalid data format'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Only POST method is allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)
