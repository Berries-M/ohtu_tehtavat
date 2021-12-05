class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

# Not, parametrina olevan ehdon negaatio (eli edellisen kohdan negaatio)
class Not:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return False
        
        return True

# All, Tosi kaikille pelaajille
class All:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

# HasFewerThan, HasAtLeast negaatio
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        #Huom! vain pienempi
        return player_value < self._value

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        is_found = False

        # Jos mikä vaan ehto totetuuu
        for matcher in self._matchers:
            if matcher.matches(player):
                is_found = True
                break

        return is_found