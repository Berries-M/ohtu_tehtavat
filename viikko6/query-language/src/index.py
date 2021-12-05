from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from query_builder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    #Tehtävä 4, ehdot annetaan oliolle
    query = QueryBuilder()
    matcher_8 = query.build()

    #for player in stats.matches(matcher_8):
        #print(player)

    matcher_9 = (
         query
         .playsIn("NYR")
         .build()
    )

    #for player in stats.matches(matcher_9):
        #print(player)

    matcher_10= (
      query  
        .playsIn("NYR")  
        .hasAtLeast(5, "goals")  
        .hasFewerThan(10, "goals")  
        .build() 
    )

    for player in stats.matches(matcher_10):
        print(player)


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
    
    #for player in stats.matches(matcher_4):
        #print(player)

    matcher_5 = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )
    
    #for player in stats.matches(matcher_5):
        #print(player)

    matcher_6 = Or(
        HasAtLeast(30, "goals"),
        HasAtLeast(50, "assists")
    )

    #for player in stats.matches(matcher_6):
        #print(player)

    matcher_7 = And(
    HasAtLeast(40, "points"),
    Or(
        PlaysIn("NYR"),
        PlaysIn("NYI"),
        PlaysIn("BOS")
    )
    )

    #for player in stats.matches(matcher_7):
        #print(player)

if __name__ == "__main__":
    main()
