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
    starting_goalkeeper = player_repository.select(int(starting_goalkeeper_id))
    starting_goalkeeper.team = new_team
    player_repository.update(starting_goalkeeper)

    backup_goalkeeper_id = request.form['backupgoalkeeper']
    backup_goalkeeper = player_repository.select(int(backup_goalkeeper_id))
    backup_goalkeeper.team = new_team
    player_repository.update(backup_goalkeeper)

    defender_1_id = request.form['defence1']
    defender_1 = player_repository.select(int(defender_1_id))
    defender_1.team = new_team
    player_repository.update(defender_1)

    defender_2_id = request.form['defence2']
    defender_2 = player_repository.select(int(defender_2_id))
    defender_2.team = new_team
    player_repository.update(defender_2)

    defender_3_id = request.form['defence3']
    defender_3 = player_repository.select(int(defender_3_id))
    defender_3.team = new_team
    player_repository.update(defender_3)

    defender_4_id = request.form['defence4']
    defender_4 = player_repository.select(int(defender_4_id))
    defender_4.team = new_team
    player_repository.update(defender_4)

    right_wing_1_id = request.form['rightwing1']
    right_wing_1 = player_repository.select(int(right_wing_1_id))
    right_wing_1.team = new_team
    player_repository.update(right_wing_1)

    right_wing_2_id = request.form['rightwing2']
    right_wing_2 = player_repository.select(int(right_wing_2_id))
    right_wing_2.team = new_team
    player_repository.update(right_wing_2)

    left_wing_1_id = request.form['leftwing1']
    left_wing_1 = player_repository.select(int(left_wing_1_id))
    left_wing_1.team = new_team
    player_repository.update(left_wing_1)

    left_wing_2_id = request.form['leftwing2']
    left_wing_2 = player_repository.select(int(left_wing_2_id))
    left_wing_2.team = new_team
    player_repository.update(left_wing_2)

    center_1_id = request.form['center1']
    center_1 = player_repository.select(int(center_1_id))
    center_1.team = new_team
    player_repository.update(center_1)

    center_2_id = request.form['center2']
    center_2 = player_repository.select(int(center_2_id))
    center_2.team = new_team
    player_repository.update(center_2)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>/delete", methods=["POST"])
def delete_team(id):
    current_team = team_repository.select(id)
    new_team = team_repository.select(17)
    players = team_repository.players(current_team)
    for player in players:
        player.team = new_team
        player_repository.update(player)
    # pdb.set_trace()
    team_repository.delete(id)
    return redirect("/teams")