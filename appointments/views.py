from django.shortcuts import render
from rest_framework import generics

from .models import Appointment
from .serializers import AppointmentSerializer
from .permissions import IsApptUserOrReadOnly

# Create your views here.
class AppointmentList(generics.ListCreateAPIView):
  queryset = Appointment.objects.all()
  serializer_class = AppointmentSerializer

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsApptUserOrReadOnly,)
  queryset = Appointment.objects.all()
  serializer_class = AppointmentSerializer