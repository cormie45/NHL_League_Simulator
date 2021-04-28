import pdb
from db.run_sql import run_sql

from models.team import Team
from models.player import Player
from models.match import Match
import repositories.team_repository as team_repository

def save(match):
    sql = "INSERT INTO matches (home_team_id, home_first_goals, str_home_first_scorers, home_second_goals, str_home_second_scorers, home_third_goals, str_home_third_scorers, home_team_score, away_team_id, away_first_goals, str_away_first_scorers, away_second_goals, str_away_second_scorers, away_third_goals, str_away_third_scorers, away_team_score, winner) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [match.home_team.id, match.home_first_goals, match.str_home_first_scorers, match.home_second_goals, match.str_home_second_scorers, match.home_third_goals, match.str_home_third_scorers, match.home_team_score, match.away_team.id, match.away_first_goals, match.str_away_first_scorers, match.away_second_goals, match.str_away_second_scorers, match.away_third_goals, match.str_away_third_scorers, match.away_team_score, match.winner]
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
        match = Match(home_team, row['home_first_goals'], row['str_home_first_scorers'], row['home_second_goals'], row['str_home_second_scorers'], row['home_third_goals'], row['str_home_third_scorers'], row['home_team_score'], away_team, row['away_first_goals'], row['str_away_first_scorers'], row['away_second_goals'], row['str_away_second_scorers'], row['away_third_goals'], row['str_away_third_scorers'],  row['away_team_score'], row['winner'], row['id'])
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
        match = Match(home_team, result['home_first-goals'], result['str_home_first_scorers'], result['home_second_goals'], result['str_home_second_scorers'], result['home_third_goals'], result['str_home_third_scorers'], result['home_team_score'], away_team, result['away_first-goals'], result['str_away_first_scorers'], result['away_second_goals'], result['str_away_second_scorers'], result['away_third_goals'], result['str_away_third_scorers'],  result['away_team_score'], result['winner'], result['id'])
    return match

def update(match):
    sql = "UPDATE matches SET (home_team_id, home_first_goals, str_home_first_scorers, home_second_goals, str_home_second_scorers, home_third_goals, str_home_third_scorers, home_team_score, away_team_id, away_first_goals, str_away_first_scorers, away_second_goals, str_away_second_scorers, away_third_goals, str_away_third_scorers, away_team_score, winner) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [match.home_team.id, match.home_first_goals, match.str_home_first_scorers, match.home_second_goals, match.str_home_second_scorers, match.home_third_goals, match.str_home_third_scorers, match.home_team_score, match.away_team.id, match.away_first_goals, match.str_away_first_scorers, match.away_second_goals, match.str_away_second_scorers, match.away_third_goals, match.str_away_third_scorers, match.away_team_score, match.winner]
    run_sql(sql, values)
    return match

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)