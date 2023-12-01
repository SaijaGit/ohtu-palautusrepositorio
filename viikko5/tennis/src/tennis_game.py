class TennisGame:

    EVEN_SITUATIONS = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]
    SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0


    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1


    def game_even(self):
        return self.player1_score == self. player2_score

    def get_even_situations(self):
        return self.EVEN_SITUATIONS[min(self.player1_score, 3)]
    
    def is_somebody_near_to_win(self):
        return self.player1_score >= 4 or self.player2_score >= 4
    
    def get_score_difference(self):
        return abs(self.player1_score - self. player2_score)
    
    def advantage_or_win(self):
        if self.get_score_difference() == 1:
            return "Advantage "
        return "Win for "
    
    def who_is_in_the_lead(self):
        score_difference = self.player1_score - self. player2_score
        if score_difference > 0:
            return self.player1_name
        return self.player2_name
    





    def get_score(self):

        if self.game_even():
            return self.get_even_situations()
        
        if self.is_somebody_near_to_win():
            return self.advantage_or_win() + self.who_is_in_the_lead()

        return self.SCORES[self.player1_score] + "-" + self.SCORES[self.player2_score]


        
