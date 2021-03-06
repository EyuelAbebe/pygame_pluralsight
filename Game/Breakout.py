__author__ = 'eyuelabebe'

import pygame
from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants


class Breakout(object):

    def __init__(self):
        self.__lives = 5
        self.__score = 0

        self.__level = Level(self)
        self.__level.load(0)

        self.__pad = Pad((0, 0), 0)
        self.__balls = [
            Ball((0, 0), 0, self)
        ]

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Game Programming with Python and Pygame")

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

        pygame.mouse.set_visible(0)

        self.__scenes = (
            PlayingGameScene(self),
            MenuScene(self),
            HighScoreScene(self),
            GameOverScene(self)
        )

        self.__currentScene = 0

        self.__sounds = ()

    def start(self):
        while 1:
            self.__clock.tick(60)

            self.screen.fill((0, 0, 0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()

            pygame.display.update()

    def changeScene(self, scene):
        pass

    def getLevel(self):
        pass

    def getScore(self):
        pass

    def increaseScore(self, score):
        pass

    def getLives(self):
        pass

    def getBalls(self):
        pass

    def getPad(self):
        pass

    def playSound(self, soundClip):
        pass

    def reduceLives(self):
        pass

    def increaseLives(self):
        pass

    def reset(self):
        pass

Breakout().start()