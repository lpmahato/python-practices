class Game:
    def __init__(self, name):
        self.name = name


    def get_games(self):
        return self.name




game = Game('Football')
print(game.get_games())