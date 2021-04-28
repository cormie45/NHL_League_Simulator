import pdb
from db.run_sql import run_sql

from models.team import Team
from models.player import Player
from models.match import Match
import repositories.team_repository as team_repository

def save(match):
    sql = "INSERT INTO matches (home_team_id, home_first_goals, home_second_goals, home_third_goals, home_team_score, away_team_id, away_first_goals, away_second_goals, away_third_goals, away_team_score, winner) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [match.home_team.id, match.home_first_goals, match.home_second_goals, match.home_third_goals, match.home_team_score, match.away_team.id, match.away_first_goals, match.away_second_goals, match.away_third_goals, match.away_team_score, match.winner]
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
        match = Match(home_team, row['home_first_goals'], row['home_second_goals'], row['home_third_goals'], row['home_team_score'], away_team, row['away_first_goals'], row['away_second_goals'], row['away_third_goals'],  row['away_team_score'], row['winner'], row['id'])
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
        match = Match(home_team, result['home_first-goals'], result['home_second_goals'], result['home_third_goals'], result['home_team_score'], away_team, result['away_first-goals'], result['away_second_goals'], result['away_third_goals'],  result['away_team_score'], result['winner'], result['id'])
    return match

def update(match):
    sql = "UPDATE matches SET (home_team_id, home_first_goals, home_second_goals, home_third_goals, home_team_score, away_team_id, away_first_goals, away_second_goals, away_third_goals, away_team_score, winner) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [match.home_team.id, match.home_first_goals, match.home_second_goals, match.home_third_goals, match.home_team_score, match.away_team.id, match.away_first_goals, match.away_second_goals, match.away_third_goals, match.away_team_score, match.winner, match.id]
    run_sql(sql, values)
    return match

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)