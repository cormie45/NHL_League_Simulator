import pdb
from flask import Blueprint, Flask, render_template, redirect, request
from models.team import Team
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)

@teams_blueprint.route("/teams/<id>")
def show_team(id):
    team = team_repository.select(id)
    players = team_repository.players(team)
    return render_template("teams/show.html", team=team, players=players)

@teams_blueprint.route("/teams/new")
def new_team():
    unattached = team_repository.select(17)
    players = team_repository.players(unattached)
    pdb.set_trace()
    return render_template("teams/new.html", players=players)

@teams_blueprint.route("/teams", methods=['POST'])
def create_team():
    name = request.form['name']
    coach = request.form['coach']
    stadium = request.form['stadium']
    city = request.form['city']
    new_team = Team(name, coach, stadium, city)
    team_repository.save(new_team)

    starting_goalkeeper_id = request.form['startinggoalkeeper']
    # pdb.set_trace()
    starting_goalkeeper = player_repository.select(int(starting_goalkeeper_id))
    starting_goalkeeper.team = new_team
    player_repository.update(starting_goalkeeper)
    return redirect("/teams")