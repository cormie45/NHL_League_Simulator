from db.run_sql import run_sql

from models.player import Player
from models.match import Match
from models.goal import Goal
import repositories.player_repository as player_repository
import repositories.match_repository as match_repository

def save(goal):
    sql = "INSERT INTO goals (match_id, player_id, period) VALUES (%s, %s, %s) RETURNING id"
    values = [goal.match.id, goal.player.id, goal.period]
    results = run_sql(sql, values)
    id = results[0]['id']
    goal.id = id

def delete_all():
    sql = "DELETE FROM goals"
    run_sql(sql)