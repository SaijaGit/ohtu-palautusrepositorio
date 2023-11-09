class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        players = self.player_reader.get_players()
        players_by_nationality = filter(lambda player: player.nationality == nationality, players)
        players_by_points = sorted(players_by_nationality, key=lambda player: player.points, reverse=True)
        return players_by_points