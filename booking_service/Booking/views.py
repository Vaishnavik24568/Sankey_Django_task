import genericpath
from http.client import BAD_REQUEST, METHOD_NOT_ALLOWED, OK
from django.shortcuts import render ,HttpResponse
from rest_framework.views import APIView
from .serializers import BookingSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import json
from rest_framework.exceptions import ParseError
from json.decoder import JSONDecodeError
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .models import Booking
from .serializers import BookingSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


class BookingListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'items_per_page'
    max_page_size = 100

class BookingListAPIView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = BookingListPagination
    ordering_fields = ['ticket_id', 'trip_id']
    filter_backends = [filters.SearchFilter]
    search_fields = ['ticket_id', 'trip_id', 'traveler_name']

class BookingDetailAPIView(APIView):
    def get_object(self, ticket_id):
        try:
            return Booking.objects.get(ticket_id=ticket_id)
        except Booking.DoesNotExist:
            raise Http404("Booking not found")

    def get(self, request, ticket_id, format=None):
        try:
            booking = self.get_object(ticket_id)
            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404 as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def index(request):
    return HttpResponse("Welcome to the Home page")

@csrf_exempt
def create(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request
            booking_data = JSONParser().parse(request)
            
            # Serialize and validate the booking data
            booking_serializer = BookingSerializer(data=booking_data)
            if booking_serializer.is_valid():
                booking_serializer = booking_serializer.save()
                return JsonResponse({'message': ' trip  Booking created successfully'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse(booking_serializer.errors, status=400)
        except (JSONDecodeError, ParseError):
            return HttpResponse("Invalid JSON data", status=400)
    else:
        return HttpResponse("Only POST method is allowed", status=405)