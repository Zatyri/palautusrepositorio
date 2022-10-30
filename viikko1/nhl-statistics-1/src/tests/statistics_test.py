import statistics
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

    def test_loyda_pelaaja(self):
        self.assertEqual(type(self.statistics.search("Semenko")), Player )
        self.assertEqual(self.statistics.search("Semenko").name, "Semenko" )
    
    def test_pelaajaa_ei_loydy(self):
        self.assertEqual(self.statistics.search("Selänne"), None)

    def test_etsi_joukkueen_perusteella(self):
        self.assertEqual(len(self.statistics.team("PIT")), 1)

    def test_etsi_tehokkain_pelaaja(self):
        self.assertEqual(self.statistics.top(1)[0].name, "Gretzky")