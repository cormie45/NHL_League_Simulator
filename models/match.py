import random
class Match:

    def __init__(self, home_team, home_first_goals, str_home_first_scorers, home_second_goals, str_home_second_scorers, home_third_goals, str_home_third_scorers, home_team_score, away_team, away_first_goals, str_away_first_scorers, away_second_goals, str_away_second_scorers, away_third_goals, str_away_third_scorers, away_team_score, winner, id=None):
        self.home_team = home_team
        self.home_first_goals = home_first_goals
        self.str_home_first_scorers = str_home_first_scorers
        self.home_second_goals = home_second_goals
        self.str_home_second_scorers = str_home_second_scorers
        self.home_third_goals = home_third_goals
        self.str_home_third_scorers = str_home_third_scorers
        self.home_team_score = home_team_score
        self.away_team = away_team
        self.away_first_goals = away_first_goals
        self.str_away_first_scorers = str_away_first_scorers
        self.away_second_goals = away_second_goals
        self.str_away_second_scorers = str_away_second_scorers
        self.away_third_goals = away_third_goals
        self.str_away_third_scorers = str_away_third_scorers
        self.away_team_score = away_team_score
        self.winner = winner
        self.id = id

    def generate_fixtures(self, teams):
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