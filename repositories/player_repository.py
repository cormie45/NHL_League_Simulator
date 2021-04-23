from db.run_sql import run_sql

from models.team import Team
from models.player import Player
from models.match import Match

def save(player):
    sql = "INSERT INTO players (first_name, last_name, age, team_id, position, points) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [player.first_name, player.last_name, player.age, player.team.id, player.position, player.points]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)