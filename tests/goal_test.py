import unittest
from models.goal import Goal
from models.match import Match
from models.player import Player

class TestGoal(unittest.TestCase):
    def setUp(self):
        self.match = Match('team_a', 1, 2, 3, 6, 'team_b', 2, 0, 1, 3, 'team_a')
        self.player = Player('steven', 'cormack', 37, 'team_a', 'center', 12)
        self.period = 2
        self.goal = Goal(self.match, self.player, self.period)

    def test_goal_has_player(self):
        self.assertEqual('steven cormack', f"{self.goal.player.first_name} {self.goal.player.last_name}")
    
    def test_goal_has_match(self):
        self.assertEqual('team_a', self.goal.match.home_team)

    def test_goal_has_period(self):
        self.assertEqual('2', self.goal.period)