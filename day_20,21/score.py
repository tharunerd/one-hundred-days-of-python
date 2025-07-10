import turtle

class Scoreboard(turtle.Turtle):  # Inheriting from Turtle class
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.update_scoreboard()  # Call this method to display the initial score

    def update_scoreboard(self):
        """Clear and rewrite the score"""
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """Increase the score and update display"""
        self.score += 1
        self.update_scoreboard()



    def game_over(self):
        """Display game over message"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
        self.goto(0, -30)
        self.write(f"Final Score: {self.score}", align="center", font=("Arial", 18, "normal"))