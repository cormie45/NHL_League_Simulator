import pdb
from models.team import Team
from models.player import Player
from models.match import Match

import repositories.match_repository as match_repository
import repositories.player_repository as player_repository
import repositories.team_repository as team_repository

match_repository.delete_all()
player_repository.delete_all()
team_repository.delete_all()

unattached = Team("Unattached", " ", " ", " ")
team_repository.save(unattached)

# Honda West

team_1 = Team("Colorado Avalanche", "Jared Bednar", "Pepsi Center", "Denver, CO")
team_repository.save(team_1)

player_1 = Player("Nathan", "MacKinnon", 25, team_1, "Center", 0)
player_repository.save(player_1)
player_2 = Player("Nazem", "Kadri", 30, team_1, "Center", 0)
player_repository.save(player_2)
player_3 = Player("Gabriel", "Landeskog", 28, team_1, "Left Wing", 0)
player_repository.save(player_3)
player_4 = Player("Andre", "Burakovsky", 26, team_1, "Left Wing", 0)
player_repository.save(player_4)
player_5 = Player("Mikko", "Rantanen", 24, team_1, "Right Wing", 0)
player_repository.save(player_5)
player_6 = Player("Joonas", "Donskoi", 29, team_1, "Right Wing", 0)
player_repository.save(player_6)
player_7 = Player("Erik", "Johnson", 33, team_1, "Defence", 0)
player_repository.save(player_7)
player_8 = Player("Cale", "Makar", 22, team_1, "Defence", 0)
player_repository.save(player_8)
player_9 = Player("Devon", "Toews", 27, team_1, "Defence", 0)
player_repository.save(player_9)
player_10 = Player("Samuel", "Girard", 22, team_1, "Defence", 0)
player_repository.save(player_10)
player_11 = Player("Phillip", "Grubauer", 29, team_1, "Goalkeeper", 0)
player_repository.save(player_11)
player_12 = Player("Pavel", "Francouz", 30, team_1, "Goalkeeper", 0)
player_repository.save(player_12)

team_2 = Team("Minnesota Wild", "Dean EVason", "Xcel Energy Center", "St. Paul, MN")
team_repository.save(team_2)

player_13 = Player("Joel", "Eriksson Ek", 24, team_2, "Center", 0)
player_repository.save(player_13)
player_14 = Player("Victor", "Rask", 28, team_2, "Center", 0)
player_repository.save(player_14)
player_15 = Player("Kirill", "Kaprizov", 23, team_2, "Left Wing", 0)
player_repository.save(player_15)
player_16 = Player("Zach", "Parise", 36, team_2, "Left Wing", 0)
player_repository.save(player_16)
player_17 = Player("Mats", "Zuccarello", 33, team_2, "Right Wing", 0)
player_repository.save(player_17)
player_18 = Player("Ryan", "Hartman", 26, team_2, "Right Wing", 0)
player_repository.save(player_18)
player_19 = Player("Jonas", "Brodin", 27, team_2, "Defence", 0)
player_repository.save(player_19)
player_20 = Player("Jared", "Spurgeon", 31, team_2, "Defence", 0)
player_repository.save(player_20)
player_21 = Player("Ryan", "Suter", 36, team_2, "Defence", 0)
player_repository.save(player_21)
player_22 = Player("Carson", "Soucy", 26, team_2, "Defence", 0)
player_repository.save(player_22)
player_23 = Player("Cam", "Talbot", 33, team_2, "Goalkeeper", 0)
player_repository.save(player_23)
player_24 = Player("Kaapo", "Kahkonen", 24, team_2, "Goalkeeper", 0)
player_repository.save(player_24)

team_3 = Team("St. Louis Blues", "Craig Berube", "Enterprise Center", "St. Louis, MO")
team_repository.save(team_3)



team_4 = Team("Anaheim Ducks", "Dallas Eakins", "Honda Center", "Anaheim, CA")
team_repository.save(team_4)



# Discover Central

team_5 = Team("Carolina Hurricanes", "Rod Brind'Amour", "PNC Arena", "Raleigh, NC")
team_repository.save(team_5)



team_6 = Team("Dallas Stars", "Rick Bowness", "American Airlines Center", "Dallas, TX")
team_repository.save(team_6)



team_7 = Team("Chicago Blackhawks", "Jeremy Colliton", "United Center", "Chicago, IL")
team_repository.save(team_7)



team_8 = Team("Detroit Red Wings", "Jeff Blashill", "Little Caesars Arena", "Detroit, MI")
team_repository.save(team_8)



# MassMutual East

team_9 = Team("Washington Capitals", "Peter Laviolette", "Capital One Arena", "Washington, DC")
team_repository.save(team_9)



team_10 = Team("Boston Bruins", "Bruce Cassidy", "TD Garden", "Boston, MA")
team_repository.save(team_10)



team_11 = Team("New York Rangers", "David Quinn", "Madison Square Garden", "Ney York, NY")
team_repository.save(team_11)



team_12 = Team("Philadelphia Flyers", "Alain Vigneault", "Wells Fargo Center", "Philadelphia, PA")
team_repository.save(team_12)



# Scotia North

team_13 = Team("Toronto Maple Leafs", "Sheldon Keefe", "Scotiabank Arena", "Toronto, ON")
team_repository.save(team_13)



team_14 = Team("Winnipeg Jets", "Paul Maurice", "Bell MTS Place", "Winnipeg, MB")
team_repository.save(team_14)



team_15 = Team("Calgary Flames", "Darryl Sutter", "Scotiabank Saddledome", "Calgary, AB")
team_repository.save(team_15)



team_16 = Team("Vancouver Canucks", "Travis Green", "Rogers Arena", "Vancouver, BC")
team_repository.save(team_16)