import pdb
from flask import Blueprint, Flask, render_template, redirect, request
from models.player import Player
import repositories.player_repository as player_repository
import repositories.team_repository as team_repository

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    teams = team_repository.select_all()
    return render_template("players/index.html", teams=teams, players=players)

@players_blueprint.route("/players/<id>")
def show_player(id):
    player = player_repository.select(id)
    teams = team_repository.select_all()
    return render_template("players/show.html", player=player, teams=teams)

@players_blueprint.route("/players/new")
def new_player():
    teams = team_repository.select_all()
    return render_template("players/new.html", teams=teams)

@players_blueprint.route("/players", methods=['POST'])
def create_player():
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    age = request.form['age']
    player_age = int(age)
    unattached = team_repository.select(17)
    position = request.form['position']
    points = 0
    new_player = Player(first_name, last_name, player_age, unattached, position, points)
    player_repository.save(new_player)
    return redirect("/players")

@players_blueprint.route("/players/<id>/edit")
def edit_player(id):
    player = player_repository.select(id)
    teams = team_repository.select_all()
    return render_template('players/edit.html', teams=teams, player=player)

@players_blueprint.route("/players/<id>", methods=["POST"])
def update_player(id):
    player = player_repository.select(id)
    team = team_repository.select(player.team.id)
    first_name = request.form['newfirstname']
    last_name = request.form['newlastname']
    age = request.form['newage']
    player_age = int(age)
    position = request.form['newposition']
    points = 0
    player = Player(first_name, last_name, player_age, team, position, points, id)
    player_repository.update(player)
    return redirect("/players")

@players_blueprint.route("/players/<id>/delete", methods=["POST"])
def delete_player(id):
    player_repository.delete(id)
    return redirect("/players")