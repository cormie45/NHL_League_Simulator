class Match:

    def __init__(self, date, home_team, home_team_score, away_team, away_team_score, winner, id=None):
        self.date = date
        self.home_team = home_team
        self.home_team_score = home_team_score
        self.away_team = away_team
        self.away_team_score = away_team_score
        self.winner = winner
        self.id = id