class Player:

    def __init__(self, first_name, last_name, age, team, position, points, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.team = team
        self.position = position
        self.points = points

    def full_name(self):
        return f"{self.first_name} {self.last_name}"