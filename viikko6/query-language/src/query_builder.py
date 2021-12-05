from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self):
        self._matchers = All()
        pass

    def build(self):
        return self._matchers

    def playsIn(self, team):
        # And(), jotta aiemmat ehdot huomioidaan
        self._matchers = And(PlaysIn(team), self._matchers)
        #Huom! Tämä palautus, jotta voi tehdä uusia ehtoja
        return self

    def hasAtLeast(self, value, attr):
        self._matchers = And(HasAtLeast(value, attr), self._matchers)
        #Huom! Tämä palautus, jotta voi tehdä uusia ehtoja
        return self

    def hasFewerThan(self, value, attr):
        self._matchers = And(HasFewerThan(value, attr), self._matchers)
        #Huom! Tämä palautus, jotta voi tehdä uusia ehtoja
        return self