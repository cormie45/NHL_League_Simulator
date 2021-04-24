from flask import Blueprint, Flask, render_template, redirect, request
from models.match import Match
import repositories.match_repository as match_repository

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()
    return render_template("matches/index.html", matches=matches)