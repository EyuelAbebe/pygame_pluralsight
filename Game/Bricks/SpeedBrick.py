__author__ = 'eyuelabebe'

from Game.Bricks import Brick


class SpeedBrick(Brick, object):

    def __init__(self, position, sprite, game):
        super(SpeedBrick, self).__init__(position, sprite, game)

    