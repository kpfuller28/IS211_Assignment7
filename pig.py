import random

random.seed(0)


class Player:
    def __init__(self, name):
        self.name   = name
        self.score = 0
        self.turnScore = 0

    def hold(self):
        self.score += self.turnScore
        self.resetTurnScore()

    def resetTurnScore(self):
        self.turnScore = 0

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return  random.randint(1, self.sides)

class Game:
    def __init__(self, player1Name, player2Name):
        self.die = Die(6)
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)
        self.currentPlayer =  self.player1
        self.gameOver = False

    def switchTurn(self):
        self.currentPlayer = self.player1 if self.currentPlayer == self.player2 else self.player2

    def takeTurn(self):
        while not self.gameOver:
            self.scoreboard()
            print(f"{self.currentPlayer.name}'s turn!")
            result = self.die.roll()
            print(f'{self.currentPlayer.name} rolled a {result}')

            if result == 1:
                print(f"Oh no! Your turn is over! You lost {self.currentPlayer.turnScore} points!")
                self.currentPlayer.resetTurnScore()
                input('Input any key to pass the dice ')
                self.switchTurn()
                break
            else:
                self.currentPlayer.turnScore += result
                if self.currentPlayer.score + self.currentPlayer.turnScore >= 100:
                    self.currentPlayer.score += self.currentPlayer.turnScore
                    self.gameEnd()
                    self.gameOver = True
                    return
                print(f"{self.currentPlayer.name}'s score this turn {self.currentPlayer.turnScore}")

                decision = input(f"{self.currentPlayer.name}, would you like to roll again or hold? Press r to roll or h to hold ")
                if decision == 'h':
                    print(f"{self.currentPlayer.name} holds with a turn score of {self.currentPlayer.turnScore}")
                    self.currentPlayer.hold()
                    input('Input any key to pass the die ')
                    self.switchTurn()
                    break

    def gameEnd(self):

        print(f"{self.currentPlayer.name} has won with a score of {self.currentPlayer.score}!")
        self.scoreboard()


    def scoreboard(self):

        print('-------------------------------------------')
        print('SCOREBOARD')
        print(f"{self.player1.name}: {self.player1.score}")
        print(f"{self.player2.name}: {self.player2.score}")
        print('-------------------------------------------')






def main():

    player1Name = input('Input Player 1 name: ')
    player2Name = input('Input Player 2 name: ')
    game = Game(player1Name, player2Name)
    while not game.gameOver:
        game.takeTurn()


if __name__ == "__main__":
    pass


main()