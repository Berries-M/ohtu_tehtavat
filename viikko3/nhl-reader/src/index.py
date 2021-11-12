from typing import Final
from datetime import date
import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games'],
        )

        if player_dict['nationality'] == "FIN":
            players.append(player)

    # Lajitellaan pelaajat pisteiden mukaiseen järjestykseen.
    sorted_players = sorted(players, key=lambda x: x.points, reverse=True)


    today = date.today()
    today2 = today.strftime("%d/%m/%Y")
    print("Suomalaisten pelaajien saldot " + today2 + ":")

    for player in sorted_players:
        print(player)

if __name__ == "__main__":
    main()
    