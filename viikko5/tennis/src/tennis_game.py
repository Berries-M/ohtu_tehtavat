class TennisGame:
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

    def get_score(self):
        if self.player1_score == self.player2_score and self.player1_score <= 4:
            score = self.points_even_both_max_4_points()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.points_not_even_another_min_4_points()

        else:
            score = self.points_not_even_both_max_3_points()

        return score

    def points_even_both_max_4_points (self):
            if self.player1_score == 0:
                score = "Love-All"
            elif self.player1_score == 1:
                score = "Fifteen-All"
            elif self.player1_score == 2:
                score = "Thirty-All"
            elif self.player1_score == 3:
                score = "Forty-All"
            else:
                score = "Deuce"

            return score

    def points_not_even_another_min_4_points (self):
            minus_result = self.player1_score - self.player2_score

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"

            return score

    def points_not_even_both_max_3_points(self):
        temp_score = 0
        score = ""
        for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score = score + "-"
                    temp_score = self.player2_score

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score