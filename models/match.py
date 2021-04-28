class Match:

    def __init__(self, home_team, home_first_goals, home_second_goals, home_third_goals, home_team_score, away_team, away_first_goals, away_second_goals, away_third_goals, away_team_score, winner, id=None):
        self.home_team = home_team
        self.home_first_goals = home_first_goals
        self.home_second_goals = home_second_goals
        self.home_third_goals = home_third_goals
        self.home_team_score = home_team_score
        self.away_team = away_team
        self.away_first_goals = away_first_goals
        self.away_second_goals = away_second_goals
        self.away_third_goals = away_third_goals
        self.away_team_score = away_team_score
        self.winner = winner
        self.id = id