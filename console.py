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

player_25 = Player("Ryan", "O'Reilly", 20, team_3, "Center", 0)
player_repository.save(player_25)
player_26 = Player("Brayden", "Schenn", 29, team_3, "Center", 0)
player_repository.save(player_26)
player_27 = Player("David", "Perron", 32, team_3, "Left Wing", 0)
player_repository.save(player_27)
player_28 = Player("Jaden", "Schwartz", 28, team_3, "Left Wing", 0)
player_repository.save(player_28)
player_29 = Player("Vladimir", "Tarasenko", 29, team_3, "Right Wing", 0)
player_repository.save(player_29)
player_30 = Player("Austin", "Poganski", 25, team_3, "Right Wing", 0)
player_repository.save(player_30)
player_31 = Player("Torey", "Krug", 30, team_3, "Defence", 0)
player_repository.save(player_31)
player_32 = Player("Vince", "Dunn", 24, team_3, "Defence", 0)
player_repository.save(player_32)
player_33 = Player("Marco", "Scandella", 31, team_3, "Defence", 0)
player_repository.save(player_33)
player_34 = Player("Robert", "Bortuzzo", 32, team_3, "Defence", 0)
player_repository.save(player_34)
player_35 = Player("Jordan", "Binnington", 27, team_3, "Goalkeeper", 0)
player_repository.save(player_35)
player_36 = Player("Ville", "Husso", 26, team_3, "Goalkeeper", 0)
player_repository.save(player_36)

team_4 = Team("Anaheim Ducks", "Dallas Eakins", "Honda Center", "Anaheim, CA")
team_repository.save(team_4)

player_37 = Player("Adam", "Henrique", 31, team_4, "Center", 0)
player_repository.save(player_37)
player_38 = Player("Ryan", "Getzlaf", 35, team_4, "Center", 0)
player_repository.save(player_38)
player_39 = Player("Max", "Comtois", 22, team_4, "Left Wing", 0)
player_repository.save(player_39)
player_40 = Player("Rickard", "Rakell", 27, team_4, "Left Wing", 0)
player_repository.save(player_40)
player_41 = Player("Jakob", "Silfverberg", 30, team_4, "Right Wing", 0)
player_repository.save(player_41)
player_42 = Player("Troy", "Terry", 23, team_4, "Right Wing", 0)
player_repository.save(player_42)
player_43 = Player("Cam", "Fowler", 29, team_4, "Defence", 0)
player_repository.save(player_43)
player_44 = Player("Kevin", "Shattenkirk", 32, team_4, "Defence", 0)
player_repository.save(player_44)
player_45 = Player("Josh", "Manson", 29, team_4, "Defence", 0)
player_repository.save(player_45)
player_46 = Player("Jamie", "Drysdale", 19, team_4, "Defence", 0)
player_repository.save(player_46)
player_47 = Player("John", "Gibson", 27, team_4, "Defence", 0)
player_repository.save(player_47)
player_48 = Player("Anthony", "Stolarz", 27, team_4, "Defence", 0)
player_repository.save(player_48)

# Discover Central

team_5 = Team("Carolina Hurricanes", "Rod Brind'Amour", "PNC Arena", "Raleigh, NC")
team_repository.save(team_5)

player_49 = Player("Sebastian", "Aho", 23, team_5, "Center", 0)
player_repository.save(player_49)
player_50 = Player("Vincent", "Trocheck", 27, team_5, "Center", 0)
player_repository.save(player_50)
player_51 = Player("Warren", "Foegele", 25, team_5, "Left Wing", 0)
player_repository.save(player_51)
player_52 = Player("Brock", "McGinn", 27, team_5, "Left Wing", 0)
player_repository.save(player_52)
player_53 = Player("Nino", "Niederreiter", 28, team_5, "Right Wing", 0)
player_repository.save(player_53)
player_54 = Player("Andrei", "Svechnikov", 21, team_5, "Right Wing", 0)
player_repository.save(player_54)
player_55 = Player("Dougie", "Hamilton", 27, team_5, "Defence", 0)
player_repository.save(player_55)
player_56 = Player("Brett", "Pesce", 26, team_5, "Defence", 0)
player_repository.save(player_56)
player_57 = Player("Jaccob", "Slavin", 26, team_5, "Defence", 0)
player_repository.save(player_57)
player_58 = Player("Brady", "Skjei", 27, team_5, "Defence", 0)
player_repository.save(player_58)
player_59 = Player("Petr", "Mrazek", 29, team_5, "Goalkeeper", 0)
player_repository.save(player_59)
player_60 = Player("Alex", "Nedeljkovic", 25, team_5, "Goalkeeper", 0)
player_repository.save(player_60)

team_6 = Team("Dallas Stars", "Rick Bowness", "American Airlines Center", "Dallas, TX")
team_repository.save(team_6)

player_61 = Player("Joe", "Pavelski", 36, team_6, "Center", 0)
player_repository.save(player_61)
player_62 = Player("Radek", "Faksa", 27, team_6, "Center", 0)
player_repository.save(player_62)
player_63 = Player("Roope", "Hintz", 24, team_6, "Left Wing", 0)
player_repository.save(player_63)
player_64 = Player("Jason", "Robertson", 21, team_6, "Left Wing", 0)
player_repository.save(player_64)
player_65 = Player("Denis", "Gurianov", 23, team_6, "Right Wing", 0)
player_repository.save(player_65)
player_66 = Player("Alexander", "Radulov", 34, team_6, "Right Wing", 0)
player_repository.save(player_66)
player_67 = Player("John", "Klingberg", 28, team_6, "Defence", 0)
player_repository.save(player_67)
player_68 = Player("Miro", "Heiskanen", 21, team_6, "Defence", 0)
player_repository.save(player_68)
player_69 = Player("Esa", "Lindell", 26, team_6, "Defence", 0)
player_repository.save(player_69)
player_70 = Player("Sami", "Vatanen", 29, team_6, "Defence", 0)
player_repository.save(player_70)
player_71 = Player("Anton", "Khudobin", 34, team_6, "Goalkeeper", 0)
player_repository.save(player_71)
player_72 = Player("Jake", "Oettinger", 22, team_6, "Goalkeeper", 0)
player_repository.save(player_72)

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