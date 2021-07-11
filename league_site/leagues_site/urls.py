from django.urls import path
from . import views

app_name = 'leagues_site'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:league_id>/teams/', views.teams, name='teams'),
    path('<int:league_id>/<int:team_id>/team_members/', views.team_members, name='team_members'),
    path('new_league/', views.new_league, name='new_league'),
    path('new_team/<int:league_id>/', views.new_team, name='new_team'),
    path('new_team_member/<int:league_id>/<int:team_id>/', views.new_team_member, name='new_team_member'),
    path('edit_league/<int:league_id>/', views.edit_league, name='edit_league'),
    path('edit_team//<int:team_id>/', views.edit_team, name='edit_team'),
    path('edit_team_member/<int:team_member_id>/', views.edit_team_member, name='edit_team_member'),
]
