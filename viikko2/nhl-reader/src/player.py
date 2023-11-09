class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team  = dict['team']
        self.nationality  = dict['nationality']
        self.goals = dict['goals']
        self.assists  = dict['assists']
        self.points = self.goals + self.assists

    def __str__(self):
        return (f"{self.name:20} {self.team}  {str(self.goals)} + "
                f"{str(self.assists)} = {str(self.points)}")