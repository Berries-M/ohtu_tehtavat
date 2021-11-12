from player import Player
from PlayerReader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        #self.players = [] Olisiko järkevää tallentaa tänne?

    def top_scorers_by_nationality(self, nationality):
        players_list = []
        players_list = self.reader.get_players()
        players_nationality = []

    # Poimitaan haluttu kansalaisuus
        for Player in players_list:
            if Player.nationality == nationality:
                players_nationality.append(Player)
                
    # Lajitellaan pelaajat pisteiden mukaiseen järjestykseen.
        sorted_players = sorted(players_nationality, key=lambda x: x.points, reverse=True)
        
        return sorted_players
