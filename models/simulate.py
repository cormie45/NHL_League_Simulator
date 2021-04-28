import pdb
import random
from models.team import Team
from models.player import Player
from models.match import Match
from models.goal import Goal
import repositories.goal_repository as goal_repository
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository
import repositories.match_repository as match_repository


def generate_fixtures(teams):
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

def simulate_league(fixtures):
    all_matches = []
    for fixture in fixtures:
        for game in fixture:
            (home_id, away_id) = game
            home_team_id = int(home_id)
            home_team = team_repository.select(home_team_id)
            home_first_goals = generate_score()
            home_first_scorers = generate_goalscorers(home_team, home_first_goals)
            home_second_goals = generate_score()
            home_second_scorers = generate_goalscorers(home_team, home_first_goals)
            home_third_goals = generate_score()
            home_third_scorers = generate_goalscorers(home_team, home_first_goals)
            home_team_score = home_first_goals + home_second_goals + home_third_goals

            away_team_id = int(away_id)
            away_team = team_repository.select(away_team_id)
            away_first_goals = generate_score()
            away_first_scorers = generate_goalscorers(home_team, home_first_goals)
            away_second_goals = generate_score()
            away_second_scorers = generate_goalscorers(home_team, home_first_goals)
            away_third_goals = generate_score()
            away_third_scorers = generate_goalscorers(home_team, home_first_goals)
            away_team_score = away_first_goals + away_second_goals + away_third_goals

            if home_team_score > away_team_score:
                winner = home_team
            elif home_team_score < away_team_score:
                winner = away_team
            else:
                winner = None
            
            match = Match(home_team, home_first_goals, home_first_scorers, home_second_goals, home_second_scorers, home_third_goals, home_third_scorers, home_team_score, away_team, away_first_goals, away_first_scorers, away_second_goals, away_second_scorers, away_third_goals, away_third_scorers, away_team_score, winner)
            # match_repository.save(match)
            first_period_goals = generate_goals(match, home_first_scorers, away_first_scorers, 1)
            second_period_goals = generate_goals(match, home_second_scorers, away_second_scorers, 2)
            third_period_goals = generate_goals(match, home_third_scorers, away_third_scorers, 3)
            all_matches.append(match)
    pdb.set_trace()
    return all_matches

def generate_score():
    potential_score = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 2, 2, 0, 2, 0, 3, 0, 0, 3, 0, 3, 4, 0, 4, 0, 4]
    score = random.choice(potential_score)
    return score

def generate_goalscorers(team, goals):
    players = team_repository.players(team)
    scorers = [random.choice(players) for i in range(goals)]
    for scorer in scorers:
        scorer.points += 1
        player_repository.update(scorer)
    return scorers

def generate_goals(match, home_players, away_players, period):
    goals = []
    for player in home_players:
        goal = Goal(match, player, period)
        goal_repository.save(goal)
        goals.append(goal)
    for player in away_players:
        goal = Goal(match, player, period)
        goal_repository.save(goal)
        goals.append(goal)
    return goals