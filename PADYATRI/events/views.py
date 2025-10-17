from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Trip, Team, Participant
from .forms import TripForm, TeamForm, ParticipantForm
from django.utils import timezone

class DashboardView(TemplateView):
    template_name = 'events/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['upcoming_trips'] = Trip.objects.filter(end_date__gte=timezone.now().date())[:5]
        ctx['team_count'] = Team.objects.count()
        ctx['participant_count'] = Participant.objects.count()
        return ctx

class TripListView(ListView):
    model = Trip
    template_name = 'events/trip_list.html'
    context_object_name = 'trips'

class TripCreateView(CreateView):
    model = Trip
    form_class = TripForm
    template_name = 'events/trip_form.html'
    success_url = reverse_lazy('events:trip_list')

class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'events/team_form.html'
    success_url = reverse_lazy('events:dashboard')

class ParticipantCreateView(CreateView):
    model = Participant
    form_class = ParticipantForm
    template_name = 'events/participant_form.html'
    success_url = reverse_lazy('events:dashboard')