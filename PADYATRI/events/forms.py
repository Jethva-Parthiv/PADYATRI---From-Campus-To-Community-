from django import forms
from .models import Participant, Team, Trip

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['team','name','roll_or_emp','role','phone','emergency_contact']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['trip','district','taluka','code']

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['title','start_date','end_date']
