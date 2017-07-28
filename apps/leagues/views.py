from django.shortcuts import render, redirect
from .models import League, Team, Player
from . import team_maker
from django.http import HttpResponse
from django.template import Context
from django.contrib import messages

def index(request):
	try:
		print number
	except Exception as error:
		context = {
			"leagues": League.objects.all(),
			"teams": Team.objects.all(),
			"players": Player.objects.all(),
		}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")

def filter(request):
	if request.method == "POST":
		query = request.POST['views']
        number = int(query)

	if number == 0:
		context = {
			"leagues": League.objects.all(),
			"teams": Team.objects.all(),
			"players": Player.objects.all()}
	elif number == 1:
		context = {
			"leagues": League.objects.filter(sport='Baseball')}
	elif number == 2:
		context = {
			"leagues": League.objects.filter(name__contains='Women')}
	elif number == 3:
		context = {
			"leagues": League.objects.filter(sport__contains='Hockey')
			}
	elif number == 4:
		context = {
			"leagues": League.objects.exclude(sport='Football')
			}
	elif number == 5:
		context = {
			"leagues": League.objects.filter(name__contains='conference')
			}
	elif number == 6:
		context = {
			"leagues": League.objects.filter(name__contains='Atlantic')
			}
	elif number == 7:
		context = {
			"teams": Team.objects.filter(location='Dallas')
			}
	elif number == 8:
		context = {
			"teams": Team.objects.filter(team_name='Raptors')
			}
	elif number == 9:
		context = {
			"teams": Team.objects.filter(location__contains='City')
			}
	elif number == 10:
		context = {
			"teams": Team.objects.filter(team_name__startswith='T')
			}
	elif number == 11:
		context = {
			"teams": Team.objects.all().order_by('location')
			}
	elif number == 12:
		context = {
			"teams": Team.objects.all().order_by('team_name').reverse()
			}
	elif number == 13:
		context = {
			"players": Player.objects.filter(last_name='Cooper')
			}
	elif number == 14:
		context = {
			"players": Player.objects.filter(first_name='Joshua')
			}
	elif number == 15:
		context = {
			"players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua')
			}
	elif number == 16:
		context = {
			"players": Player.objects.filter(first_name='Alexander')|Player.objects.filter(first_name='Wyatt')}
	return render(request, "leagues/index.html", context)
