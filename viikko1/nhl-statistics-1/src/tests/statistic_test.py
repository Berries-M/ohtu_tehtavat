import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    # Tästä alkaa itse kirjoitetut

    # Etsitään nimi, jota ei ole
    def test_search_ei_ole(self):
        self.assertIsNone(self.statistics.search("Kukkuu"))

   # Tietyn pelaajan pistet
    def test_search(self):
        eka = "Semenko"
        haettu_listasta = self.statistics.search(eka).name
        self.assertEqual(eka, haettu_listasta)

    # Tietty joukkue, josta pelaajan nimi
    def test_team(self):
        joukkue = "PIT"
        haettu_listasta = self.statistics.team(joukkue)[0].name
        self.assertEqual("Lemieux", haettu_listasta)

    # Paras pelaaja
    def test_top_scorers(self):
        haettu_listasta = self.statistics.top_scorers(1)[0].name
        print(haettu_listasta)
        self.assertEqual("Gretzky", haettu_listasta)
