from db.run_sql import run_sql

from models.team import Team
from models.player import Player
from models.match import Match
import repositories.team_repository as team_repository

def save(player):
    sql = "INSERT INTO players (first_name, last_name, age, team_id, position, points) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [player.first_name, player.last_name, player.age, player.team.id, player.position, player.points]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player

def select_all():
    players = []

    sql = "SELECT * FROM players"
    results = run_sql(sql)

    for row in results:
        team = team_repository.select(row['team_id'])
        player = Player(row['first_name'], row['last_name'], row['age'], team, row['position'], row['points'])
        players.append(player)
    return players

def select(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = team_repository.select(result['team_id'])
        player = Player(result['first_name'], result['last_name'], result['age'], team, result['position'], result['points'])
    return player

def update(player):
    sql = "UPDATE players SET (first_name, last_name, age, team_id, position, points) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [player.first_name, player.last_name, player.age, player.team.id, player.position, player.points]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)