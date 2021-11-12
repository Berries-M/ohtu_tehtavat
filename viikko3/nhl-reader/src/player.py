class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = goals + assists
    
    def __str__(self):
        # Huom intit stringiksi
        return f"{self.name:23}" + f"{self.team:4}" + f"{str(self.goals):2}" + " + " + f"{str(self.assists):2}" + " = " + str(self.points)
        