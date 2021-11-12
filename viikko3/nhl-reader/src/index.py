from typing import Final
from datetime import date
from PlayerReader import PlayerReader
from PlayerStats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    today = date.today()
    today2 = today.strftime("%d/%m/%Y")
    
    print("Kyselyn tulos " + today2 + ":")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
    