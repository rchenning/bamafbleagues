from django.contrib import admin
from .models import League, Team, Team_Member

admin.site.register(League)
admin.site.register(Team)
admin.site.register(Team_Member)
