import pdb
import random
from models.team import Team
from models.player import Player
from models.match import Match
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository
import repositories.match_repository as match_repository


first_period_goals = 0
first_period_scorers = []
second_period_goals = 0
second_period_scorers = []
third_period_goals = 0
third_period_scorers = []

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
        for game in fixture:
            # pdb.set_trace()
            (home_id, away_id) = game
            home_team_id = int(home_id)
            home_team = team_repository.select(home_team_id)
            generate_score(home_team)
            home_first_goals = first_period_goals
            home_first_scorers = first_period_scorers
            home_second_goals = second_period_goals
            home_second_scorers = second_period_scorers
            home_third_goals = third_period_goals
            home_third_scorers = third_period_scorers
            home_team_score = home_first_goals + home_second_goals + home_third_goals

            away_team_id = int(away_id)
            away_team = team_repository.select(away_team_id)
            generate_score(away_team)
            away_first_goals = first_period_goals
            away_first_scorers = first_period_scorers
            away_second_goals = second_period_goals
            away_second_scorers = second_period_scorers
            away_third_goals = third_period_goals
            away_third_scorers = third_period_scorers
            away_team_score = away_first_goals + away_second_goals + away_third_goals

            if home_team_score > away_team_score:
                winner = home_team
            elif home_team_score < away_team_score:
                winner = away_team
            else:
                winner = None
            
        match = Match(home_team, home_first_goals, home_first_scorers, home_second_goals, home_second_scorers, home_third_goals, home_third_scorers, home_team_score, away_team, away_first_goals, away_first_scorers, away_second_goals, away_second_scorers, away_third_goals, away_third_scorers, away_team_score, winner)
        match_repository.save(match)
        return match

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
    first_period_goals = 0
    first_period_goals = random.choice(potential_score)
    first_period_scorers = []
    if first_period_goals == 1:
        scorer = random.choice(potential_goalscorer)
        first_period_scorers.append(scorer)
    elif first_period_goals == 2:
        scorer = random.choice(potential_goalscorer)
        first_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        first_period_scorers.append(scorer)
    elif first_period_goals == 3:
        scorer = random.choice(potential_goalscorer)
        first_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        first_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        first_period_scorers.append(scorer)
    elif first_period_goals == 4:
        scorer = random.choice(potential_goalscorer)
        first_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        first_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        first_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        first_period_scorers.append(scorer)

    second_period_goals = random.choice(potential_score)
    second_period_scorers = []
    if second_period_goals == 1:
        scorer = random.choice(potential_goalscorer)
        second_period_scorers.append(scorer)
    elif second_period_goals == 2:
        scorer = random.choice(potential_goalscorer)
        second_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        second_period_scorers.append(scorer)
    elif second_period_goals == 3:
        scorer = random.choice(potential_goalscorer)
        second_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        second_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        second_period_scorers.append(scorer)
    elif second_period_goals == 4:
        scorer = random.choice(potential_goalscorer)
        second_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        second_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        second_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        second_period_scorers.append(scorer)

    third_period_goals = random.choice(potential_score)
    third_period_scorers = []
    if third_period_goals == 1:
        scorer = random.choice(potential_goalscorer)
        third_period_scorers.append(scorer)
    elif third_period_goals == 2:
        scorer = random.choice(potential_goalscorer)
        third_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        third_period_scorers.append(scorer)
    elif third_period_goals == 3:
        scorer = random.choice(potential_goalscorer)
        third_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        third_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        third_period_scorers.append(scorer)
    elif third_period_goals == 4:
        scorer = random.choice(potential_goalscorer)
        third_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        third_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        third_period_scorers.append(scorer)
        scorer = random.choice(potential_goalscorer)
        third_period_scorers.append(scorer)

    pdb.set_trace()
    return first_period_goals, second_period_goals, third_period_goals, first_period_scorers, second_period_scorers, third_period_scorers
