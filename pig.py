import random



class Player:
    def __init__(self, name):
        self.name   = name
        self.score = 0
        self.turnScore = 0
        self.gameWins = 0

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
    def __init__(self, players):
        random.seed(0)
        self.die = Die(6)
        self.players = players
        self.currentPlayer =  self.players[0]
        self.gameOver = False
        self.turn = 0
        self.rolls = 0
        self.winner = ''

    def switchTurn(self):
        if self.players.index(self.currentPlayer) == len(self.players) - 1:
            self.currentPlayer = self.players[0]
        else:
            self.currentPlayer = self.players[self.players.index(self.currentPlayer) + 1]

    def takeTurn(self):
        self.turn += 1
        still = ''
        while not self.gameOver:
            self.scoreboard()
            print(f"{still}{self.currentPlayer.name}'s turn!")
            result = self.die.roll()
            self.rolls += 1
            print(f'{self.currentPlayer.name} rolled a: {result}')
            still = 'Still '

            if result == 1:
                print(f"Oh no! Your turn is over! You lost {self.currentPlayer.turnScore} points!")
                self.currentPlayer.resetTurnScore()
                input('Press enter to pass the die: ')
                self.switchTurn()
                break
            else:
                self.currentPlayer.turnScore += result
                if self.currentPlayer.score + self.currentPlayer.turnScore >= 100:
                    self.currentPlayer.score += self.currentPlayer.turnScore
                    self.gameEnd()
                    self.resetGame()
                    self.gameOver = True
                    return
                print(f"{self.currentPlayer.name}'s score this turn: {self.currentPlayer.turnScore}")

                decision = input(f"{self.currentPlayer.name}, would you like to roll again or hold? Press r to roll or h to hold: ")
                while decision != 'r' and decision != 'h':
                    decision = input(f"Invalid input: {decision}. Please only input r to roll again, or h to hold: ")
                if decision == 'h':
                    print(f"{self.currentPlayer.name} holds with a turn score of: {self.currentPlayer.turnScore}")
                    self.currentPlayer.hold()
                    input('Press enter to pass the die ')
                    self.switchTurn()
                    break

    def gameEnd(self):

        print(f"{self.currentPlayer.name} has won with a score of {self.currentPlayer.score}!")
        self.winner = self.currentPlayer.name
        self.currentPlayer.gameWins += 1
        self.scoreboard()

    def resetGame(self):
        for player in self.players:
            player.score = 0
            player.turnScore = 0
        self.turn = 0
        self.rolls = 0
        self.gameOver = False
        self.winner = ''


    def scoreboard(self):

        print('-------------------------------------------')
        print(f'SCOREBOARD --- Turn: {self.turn} --- Rolls: {self.rolls}')
        for player in self.players:
            if self.winner == player.name:
                print(f"{player.name}: {player.score} ---- WINNER!")
            else:
                print(f"{player.name}: {player.score}")
        print('-------------------------------------------')

class Series:
    def __init__(self, gamesToWin, players):
        self.gamesToWin = gamesToWin
        self.players = players
        self.winner = ''
        self.seriesOver = False

    def playGame(self):
        game = Game(self.players)
        self.scoreboard()
        while not game.gameOver:
            game.takeTurn()
        for player in self.players:
            if player.gameWins >= self.gamesToWin:
                self.winner = player.name
                self.seriesEnd()
                self.seriesOver = True
                return

    def scoreboard(self):
        print(f"--------- SERIES SCOREBOARD ---------")
        for player in self.players:
            if self.winner == player.name:
                print(f"{player.name} game wins: {player.gameWins} ---- SERIES WINNER")
            else:
                print(f"{player.name} game wins: {player.gameWins}")
        print(f"-------------------------------------")

    def seriesEnd(self):
        print(f"{self.winner} wins the series!")
        self.scoreboard()



def main():
    players = []
    while True:
        numberPlayers = input('How many players would you like to play Pig with: ')
        try:
            numberPlayers = int(numberPlayers)
            break
        except ValueError:
            print(f"Invalid input. Please input a number for number of players.")
    for i in range(numberPlayers):
        playerName = input(f"Please enter Player {i+1} name: ")
        players.append(Player(playerName))
    while True:
        gamesToWin = input('How many games to win the whole series: ')

        try:
            gamesToWin = int(gamesToWin)
            break
        except ValueError:
            print(f"Invalid input. Please input number for number of games to win.")
    series = Series(gamesToWin, players)
    while not series.seriesOver:
        series.playGame()




if __name__ == "__main__":
    pass


main()