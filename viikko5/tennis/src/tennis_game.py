class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):        
        if self.is_game_tie(self.player1_score, self.player2_score):
            return self.get_even_score(self.player1_score)
        
        if self.is_game_over(self.player1_score, self.player2_score):
            score_difference = self.player1_score - self. player2_score

            if self.is_advantage(score_difference):
                return "Advantage " + self.get_player_with_advantage(score_difference)
            else:
                return "Win for " + self.get_winner(score_difference)

        return self.get_player_score_as_string(self.player1_score) + "-" + self.get_player_score_as_string(self.player2_score)

    def is_game_tie(self, player1, player2):
        return player1 == player2

    def get_even_score(self, score):
        scores = ["Love-All","Fifteen-All","Thirty-All","Forty-All"]
        if score >= len(scores): 
            return "Deuce"
    
        return scores[score]
    
    def is_game_over(self, player1, player2):
        return player1 >= 4 or player2 >= 4

    def is_advantage(self, score_difference):
        return abs(score_difference) == 1

    def get_player_with_advantage(self, score_difference):
        if score_difference == 1:
            return self.player1_name
        else:
            return self.player2_name
    
    def get_winner(self, score_difference):
        if score_difference >= 2:
            return self.player1_name
        else:
            return self.player2_name 

    def get_player_score_as_string(self, player_score):
        scores = ["Love","Fifteen","Thirty","Forty"]
        return scores[player_score]

