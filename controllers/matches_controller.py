from flask import Blueprint, Flask, render_template, redirect, request
from models.match import Match
from models.team import Team
from models.player import Player
from models.simulate import generate_fixtures, simulate_league
import repositories.match_repository as match_repository
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository
import repositories.goal_repository as goal_repository

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()
    return render_template("matches/index.html", matches=matches)

@matches_blueprint.route("/matches/setup")
def setup_season():
    teams = team_repository.select_all()
    return render_template("matches/setup.html", teams=teams)

@matches_blueprint.route("/matches/<id>")
def show_match(id):
    match = match_repository.select(id)
    teams = team_repository.select_all()
    fpg = match_repository.goals(match, 1)
    spg = match_repository.goals(match, 2)
    tpg = match_repository.goals(match, 3)

    return render_template("matches/show.html", match=match, teams=teams, fpg=fpg, spg=spg, tpg=tpg)

@matches_blueprint.route("/matches/run", methods=['POST'])
def run_season():
    team_1 = request.form['team1']
    team_2 = request.form['team2']
    team_3 = request.form['team3']
    team_4 = request.form['team4']
    team_5 = request.form['team5']
    team_6 = request.form['team6']
    team_7 = request.form['team7']
    team_8 = request.form['team8']
    team_9 = request.form['team9']
    team_10 = request.form['team10']
    team_11 = request.form['team11']
    team_12 = request.form['team12']
    team_13 = request.form['team13']
    team_14 = request.form['team14']
    team_15 = request.form['team15']
    team_16 = request.form['team16']

    teams = [team_1, team_2, team_3, team_4, team_5, team_6, team_7, team_8, team_9, team_10, team_11, team_12, team_13, team_14, team_15, team_16]
    fixtures = generate_fixtures(teams)
    results = simulate_league(fixtures)

    return redirect("/")