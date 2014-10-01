__author__ = 'eyuelabebe'

from Game.Bricks import Brick


class LifeBrick(Brick, object):

    def __init__(self, position, sprite, game):
        super(LifeBrick, self).__init__(position, sprite, game)

