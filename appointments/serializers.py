from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
  class Meta:
    fields =('appt_user','appt_name','appt_date','appt_duration')
    model = Appointment
