from db.run_sql import run_sql

from models.team import Team
from models.player import Player
from models.match import Match

def save(team):
    sql = "INSERT INTO teams (name, coach, stadium, city) VALUES(%s, %s, %s, %s) RETURNING *"
    values = [team.name, team.coach, team.stadium, team.city]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team

def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['coach'], row['stadium'], row['city'], row['id'])
        teams.append(team)
    return teams

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['name'], result['coach'], result['stadium'], result['city'], result['id'])
    return team

def players(team):
    players = []

    sql = "SELECT * FROM players WHERE team_id = %s"
    values = [team.id]
    results = run_sql(sql, values)

    for row in results:
        player = Player(row['first_name'], row['last_name'], row['age'], row['team_id'], row['position'], row['points'])
        players.append(player)
    return players

def matches(team):
    matches = []

    sql = "SELECT * FROM matches WHERE home_team_id = %s OR away_team_id = %s"
    values = [team.id, team.id]
    results = run_sql(sql, values)

    for row in results:
        match = Match(row['date'], row['home_team_id'], row['home_team_score'], row['away_team_id'], row['away_team_score'], row['winner'])
        matches.append(match)
    return matches

def update(id):
    sql = "UPDATE teams SET (name, coach, stadium, city) = (%s, %s, %s, %s) WHERE id = %s"
    values = [team.name, team.coach, team.stadium, team.city, team.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)