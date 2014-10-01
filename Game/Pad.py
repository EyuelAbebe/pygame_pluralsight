__author__ = 'eyuelabebe'

from Game.Shared import *


class Pad(GameObject, object):

    def __init__(self, position, sprite):
        super(Pad, self).__init__(position, GameConstants.PAD_SIZE, sprite)

