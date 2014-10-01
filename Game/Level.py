__author__ = 'eyuelabebe'


class Level(object):

    def __init__(self, game):
        self.__game = game
        self.__bricks = []
        self.__amountOfBricks = 0
        self.currentLevel = 0

    def getBricks(self):
        return self.__bricks

    def getAmountOfBricks(self):
        return self.__amountOfBricks

    def brickHit(self):
        self.__amountOfBricks -= 1

    def loadNextLevel(self):
        pass

    def load(self, level):
        pass

