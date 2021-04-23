from db.run_sql import run_sql

from models.team import Team
from models.player import Player
from models.match import Match

def save(match):
    sql = "INSERT INTO matches (date, home_team_id, home_team_score, away_team_id, away_team_score, winner) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [match.date, match.home_team.id, match.home_team_score, match.away_team.id, match.away_team_score, match.winner]
    results = run_sql(sql, values)
    id = results[0]['id']
    match.id = id
    return match