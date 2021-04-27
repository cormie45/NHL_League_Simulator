import random
from models.team import Team
from models.player import Player
from models.match import Match
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository
import repositories.match_repository as match_repository
    
def generator(teams):
    random.shuffle(teams)
    n = len(teams)
    matches = []
    fixtures = []
    return_matches = []
    for fixture in range(1, n):
        for i in range(n//2):
            matches.append((teams[i], teams[n - 1 - i]))
            return_matches.append((teams[n - 1 - i], teams[i]))
        teams.insert(1, teams.pop())
        fixtures.insert(len(fixtures)//2, matches)
        fixtures.append(return_matches)
        matches = []
        return_matches = []

    return fixtures

def simulate(fixtures):
    for fixture in fixtures:
        home_team_id = int(fixture[0])
        home_team = team_repository.select(home_team_id)
        generate_score(home_team)

        away_team_id = int(fixture[1])
        away_team = team_repository.select(away_team_id)
        generate_score(away_team)

def generate_score(team):
    players = team_repository.players(team)
    potential_score = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 3, 0, 0, 4]
    potential_goalscorer = []
    for player in players:
        if player.position == "Defence":
            potential_goalscorer.append(player)
        if player.position == "Left Wing":
            potential_goalscorer.append(player)
            potential_goalscorer.append(player)
            potential_goalscorer.append(player)
        elif player.position == "Right Wing":
            potential_goalscorer.append(player)
            potential_goalscorer.append(player)
            potential_goalscorer.append(player)
        elif player.position == "Center":
            potential_goalscorer.append(player)
            potential_goalscorer.append(player)
            potential_goalscorer.append(player)
            potential_goalscorer.append(player)
            potential_goalscorer.append(player)
            potential_goalscorer.append(player)

    first_period_goals = random.choice(potential_score)
    scorers = []
    if first_period_goals == 1:
        scorer = random.choice(potential_goalscorer)
        scorers.append(scorer)
    elif first_period_goals == 2:
        scorer = random.choice(potential_goalscorer)
        scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        scorers.append(scorer)
    elif first_period_goals == 3:
        scorer = random.choice(potential_goalscorer)
        scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        scorers.append(scorer)