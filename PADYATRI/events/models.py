from django.db import models
from django.utils import timezone

ROLE_CHOICES = (
    ("student", "Student"),
    ("faculty", "Faculty"),
    ("staff", "Staff"),
)

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Taluka(models.Model):
    district = models.ForeignKey(District, related_name='talukas', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = (('district','name'),)

    def __str__(self):
        return f"{self.name} ({self.district.name})"

class Trip(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    trip = models.ForeignKey(Trip, related_name='teams', on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    taluka = models.ForeignKey(Taluka, blank=True, null=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=30, blank=True, help_text='Optional team code')

    def __str__(self):
        return f"Team {self.district.name} - {self.taluka.name if self.taluka else 'All'}"

class Participant(models.Model):
    team = models.ForeignKey(Team, related_name='participants', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    roll_or_emp = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    phone = models.CharField(max_length=20, blank=True)
    emergency_contact = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.role})"
