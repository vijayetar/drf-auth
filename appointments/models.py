from django.db import models
import datetime
from django.contrib.auth import get_user_model
import django.utils
from django.urls import reverse

# Create your models here.
class Appointment(models.Model):
  appt_user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
  appt_name = models.TextField('Select name of appt', max_length=10)
  appt_date = models.DateTimeField('Enter date of activity', auto_now_add=True)
  appt_duration = models.IntegerField('Enter duration in minutes', default = 0)

  def __str__(self):
    return self.appt_name
      
  def get_absolute_url(self):
    return reverse('appt_list')
