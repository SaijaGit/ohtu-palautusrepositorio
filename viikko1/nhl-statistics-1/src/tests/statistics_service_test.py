import unittest
from statistics_service import StatisticsService, sort_by_points, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Sevenkorv", "EDM", 4, 12),
            Player("Lemueux", "PIT", 45, 54),
            Player("Curry", "EDM", 37, 53),
            Player("Freezerman", "DET", 42, 56),
            Player("Greyzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    
    def test_player_search(self):
        player = self.stats.search("Sevenkorv")
        print("test1! player = ", str(player))

        self.assertEqual(str(player), str(Player("Sevenkorv", "EDM", 4, 12)))


    def test_player_search_none(self):
        player = self.stats.search("Drontti")

        self.assertEqual(player, None)

    
    def test_team_filter(self):
        team_test = []
        for player in self.stats.team("EDM"):
            team_test.append(str(player))
        
        team_compare = [
            str(Player("Sevenkorv", "EDM", 4, 12)),
            str(Player("Curry", "EDM", 37, 53)),
            str(Player("Greyzky", "EDM", 35, 89))
        ]
        self.assertListEqual(team_test, team_compare)


    def test_team_filter_empty(self):
        team_test = self.stats.team("Losers")

        self.assertListEqual(team_test, [])

        
    def test_player_sort_by_points(self):
        team_test = []
        for player in self.stats.top(2, SortBy.POINTS):
            team_test.append(str(player))

        team_compare = [
            str(Player("Greyzky", "EDM", 35, 89)), 
            str(Player("Lemueux", "PIT", 45, 54))
        ]

        self.assertListEqual(team_test, team_compare)


    def test_player_sort_by_goals(self):
        team_test = []
        for player in self.stats.top(5, SortBy.GOALS):
            team_test.append(str(player))
        
        team_compare = [
            str(Player("Lemueux", "PIT", 45, 54)),
            str(Player("Freezerman", "DET", 42, 56)),
            str(Player("Curry", "EDM", 37, 53)),
            str(Player("Greyzky", "EDM", 35, 89)),
            str(Player("Sevenkorv", "EDM", 4, 12))
        ]

        self.assertListEqual(team_test, team_compare)


    def test_player_sort_by_assists(self):
        team_test = []
        for player in self.stats.top(4, SortBy.ASSISTS):
            team_test.append(str(player))
        
        team_compare = [
            str(Player("Greyzky", "EDM", 35, 89)),
            str(Player("Freezerman", "DET", 42, 56)),
            str(Player("Lemueux", "PIT", 45, 54)),
            str(Player("Curry", "EDM", 37, 53))
        ]

        self.assertListEqual(team_test, team_compare)


    def test_player_sort_too_many(self):
        team_test = []
        for player in self.stats.top(50):
            team_test.append(str(player))
        
        team_compare = [
            str(Player("Greyzky", "EDM", 35, 89)),
            str(Player("Lemueux", "PIT", 45, 54)),
            str(Player("Freezerman", "DET", 42, 56)),
            str(Player("Curry", "EDM", 37, 53)),
            str(Player("Sevenkorv", "EDM", 4, 12))
        ]

        self.assertListEqual(team_test, team_compare)


    def test_get_player_points(self):
        points = sort_by_points(Player("Sevenkorv", "EDM", 4, 12))
        self.assertEqual(points, 16)
    

