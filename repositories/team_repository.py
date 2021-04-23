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
