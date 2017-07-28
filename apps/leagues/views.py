from django.shortcuts import render, redirect
from .models import League, Team, Player
from . import team_maker
from django.http import HttpResponse
from django.template import Context
from django.contrib import messages
from django.db.models import Count

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
	elif number == 17:
		context = {
			"teams": Team.objects.filter(league__name='Atlantic Soccer Conference')}
	elif number == 18:
		context = {
			"players": Player.objects.filter(curr_team__team_name='Penguins')}
	elif number == 19:
		context = {
			"players": Player.objects.filter(curr_team__league__name='International Collegiate Baseball Conference')
			}
	elif number == 20:
		context = {
			"players": Player.objects.filter(last_name='Lopez').filter(curr_team__league__name='American Conference of Amateur Football')
			}
	elif number == 21:
		context = {
			"players": Player.objects.filter(curr_team__league__sport='Football')
			}
	elif number == 22:
		context = {
			"teams": Team.objects.filter(curr_players__first_name='Sophia')
			}
	elif number == 23:
		context = {
			"leagues": League.objects.filter(teams__curr_players__first_name='Sophia')
			}
	elif number == 24:
		context = {
			"players": Player.objects.filter(last_name='Flores').exclude(curr_team__team_name='Roughriders')
			}
	elif number == 25:
		context = {
			"teams": Team.objects.filter(all_players__first_name='Samuel').filter(all_players__last_name='Evans')
			}
	elif number == 26:
		context = {
			"players": Player.objects.filter(all_teams__team_name='Tiger-Cats')
			}
	elif number == 27:
		context = {
			"players": Player.objects.filter(all_teams__team_name='Vikings').exclude(curr_team__team_name='Vikings')
			}
	elif number == 28:
		context = {
			"teams": Team.objects.filter(all_players__first_name='Jacob').filter(all_players__last_name='Gray').exclude(team_name='Colts')
			}
	elif number == 29:
		context = {
			"players": Player.objects.filter(first_name='Joshua').filter(all_teams__league__name='Atlantic Federation of Amateur Baseball Players')
			}
	elif number == 30:
		num_players =
		context = {
			"teams": Team.objects.annotate(num_players=Count('all_players')).exclude(num_players<12)
			# Can't get this to work. Will fix later.
			}
	elif number == 31:
		context = {
			"players": Player.objects.annotate(num_teams=Count('all_teams')).order_by('num_teams')
			}
	return render(request, "leagues/index.html", context)
