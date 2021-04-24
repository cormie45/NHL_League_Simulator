from db.run_sql import run_sql

from models.team import Team
from models.player import Player
from models.match import Match
import repositories.team_repository as team_repository

def save(match):
    sql = "INSERT INTO matches (date, home_team_id, home_team_score, away_team_id, away_team_score, winner) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [match.date, match.home_team.id, match.home_team_score, match.away_team.id, match.away_team_score, match.winner]
    results = run_sql(sql, values)
    id = results[0]['id']
    match.id = id
    return match

def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        home_team = team_repository.select(row['home_team_id'])
        away_team = team_repository.select(row['away_team_id'])
        match = Match(row['date'], home_team, row['home_team_score'], away_team, row['away_team_score'], row['winner'])
        matches.append(match)
    return matches

def select(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        home_team = team_repository.select(result['home_team_id'])
        away_team = team_repository.select(result['away_team_id'])
        match = Match(result['date'], home_team, result['home_team_score'], away_team, result['away_team_score'], result['winner'])
    return match

def update(match):
    sql = "UPDATE matches SET (date, home_team_id, home_team_score, away_team_id, away_team_score, winner) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [match.date, match.home_team.id, match.home_team_score, match.away_team.id, match.away_team_score, match.winner]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)