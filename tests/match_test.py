import unittest
from models.match import Match

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.match = Match('team_a', 1, 2, 3, 6, 'team_b', 1, 0, 3, 4, 'team_a')

    def test_has_home_team(self):
        self.assertEqual('team_a', self.match.home_team)

    def test_has_goals(self):
        self.assertEqual('6', self.match.home_team_score)

    def test_has_winner(self):
        self.assertEqual('team_a', self.match.winner)