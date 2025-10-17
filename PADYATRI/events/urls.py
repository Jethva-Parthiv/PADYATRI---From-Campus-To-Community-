from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('trips/', views.TripListView.as_view(), name='trip_list'),
    path('trips/create/', views.TripCreateView.as_view(), name='trip_create'),
    path('teams/create/', views.TeamCreateView.as_view(), name='team_create'),
    path('participants/create/', views.ParticipantCreateView.as_view(), name='participant_create'),
]
