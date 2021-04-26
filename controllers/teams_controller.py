from flask import Blueprint, Flask, render_template, redirect, request
from models.team import Team
import repositories.team_repository as team_repository

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