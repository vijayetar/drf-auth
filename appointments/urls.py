from django.urls import path
from .views import AppointmentList, AppointmentDetail


urlpatterns = [
  path('', AppointmentList.as_view(), name='appt_list'),
  path('<int:pk>/', AppointmentDetail.as_view(), name='appt_detail')
]