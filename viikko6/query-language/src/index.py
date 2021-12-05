from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    #for player in stats.matches(matcher):
        #print(player)

    matcher_2 = All(
        HasAtLeast(0, "goals"),
    )

    #for player in stats.matches(matcher_2):
        #print(player)

    matcher_3 = Not(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    #for player in stats.matches(matcher_3):
        #print(player)

    matcher_4 = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )
    
    for player in stats.matches(matcher_4):
        print(player)

    matcher_5 = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )
    
    for player in stats.matches(matcher_5):
        print(player)



if __name__ == "__main__":
    main()
