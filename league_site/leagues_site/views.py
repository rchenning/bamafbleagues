from django.shortcuts import render, redirect, get_object_or_404
from .models import League, Team, Team_Member
from .forms import LeagueForm, TeamForm, Team_MemberForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    leagues = League.objects.order_by('name')
    context = {'leagues': leagues}
    return render(request, 'leagues_site/index.html', context)


def teams(request, league_id):
    league = get_object_or_404(League, id=league_id)
    teams = league.team_set.order_by('name')
    context = {'league': league, 'teams': teams}
    return render(request, 'leagues_site/teams.html', context)


@login_required
def team_members(request, league_id, team_id):
    league = get_object_or_404(League, id=league_id)
    team = get_object_or_404(league.team_set, id=team_id)
    team_members = team.team_member_set.order_by('lastname')
    context = {'league': league, 'team': team, 'team_members': team_members}
    return render(request, 'leagues_site/team_members.html', context)


@login_required
def new_league(request):
    if request.method != 'POST':
        form = LeagueForm
    else:
        form = LeagueForm(data=request.POST)
        if form.is_valid():
            new_league = form.save(commit=False)
            new_league.owner = request.user
            new_league.save()
            return redirect('leagues_site:index')
    context = {'form': form}
    return render(request, 'leagues_site/new_league.html', context)


@login_required
def new_team(request, league_id):
    league = get_object_or_404(League, id=league_id)

    if request.method != 'POST':
        form = TeamForm()
    else:
        form = TeamForm(data=request.POST)
        if form.is_valid():
            new_team = form.save(commit=False)
            new_team.league = league
            new_team.owner = request.user
            new_team.save()
            return redirect('leagues_site:teams', league_id=league_id)
    context = {'league': league, 'form': form}
    return render(request, 'leagues_site/new_team.html', context)


@login_required
def new_team_member(request, league_id, team_id):
    league = get_object_or_404(League, id=league_id)
    team = get_object_or_404(league.team_set, id=team_id)

    if request.method != 'POST':
        form = Team_MemberForm()
    else:
        form = Team_MemberForm(data=request.POST)
        if form.is_valid():
            new_team_member = form.save(commit=False)
            new_team_member.team = team
            new_team_member.owner = request.user
            new_team_member.save()
            return redirect('leagues_site:team_members', league_id=league_id, team_id=team_id)
    context = {'league': league, 'team': team, 'form': form}
    return render(request, 'leagues_site/new_team_member.html', context)


@login_required
def edit_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    league = team.league
    if team.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = TeamForm(instance=team)
    else:
        form = TeamForm(instance=team, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('leagues_site:teams', league_id=league.id)
    context = {'league': league, 'team': team, 'form': form}
    return render(request, 'leagues_site/edit_team.html', context)


@login_required
def edit_league(request, league_id):
    league = get_object_or_404(League, id=league_id)
    if league.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = LeagueForm(instance=league)
    else:
        form = LeagueForm(instance=league, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('leagues_site:index')
    context = {'league': league, 'form': form}
    return render(request, 'leagues_site/edit_league.html', context)


@login_required
def edit_team_member(request, team_member_id):
    team_member = get_object_or_404(Team_Member, id=team_member_id)
    team = team_member.team
    league = team.league
    if team_member.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = Team_MemberForm(instance=team_member)
    else:
        form = Team_MemberForm(instance=team_member, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('leagues_site:team_members', league_id=league.id, team_id=team.id)
    context = {'league': league, 'team': team, 'team_member': team_member, 'form': form}
    return render(request, 'leagues_site/edit_team_member.html', context)
