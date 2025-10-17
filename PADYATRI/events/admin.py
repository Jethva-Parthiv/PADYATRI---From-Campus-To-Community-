from django.contrib import admin
from .models import District, Taluka, Trip, Team, Participant

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Taluka)
class TalukaAdmin(admin.ModelAdmin):
    list_display = ('name','district')
    list_filter = ('district',)
    search_fields = ('name',)

class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 1

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('district','taluka','trip','code')
    list_filter = ('district','trip')
    inlines = (ParticipantInline,)

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title','start_date','end_date')
    inlines = ()

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name','role','team')
    list_filter = ('role','team__district')
    search_fields = ('name','roll_or_emp')