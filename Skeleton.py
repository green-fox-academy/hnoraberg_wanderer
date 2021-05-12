from random import randint
from Enemy import Enemy

class Skeleton(Enemy):

    def __init__(self, x, y, level=1, is_keyholder=False):
        super().__init__(x, y, level, is_keyholder)
        self.x = x
        self.y = y
        self.name = "skeleton"
        self.hp = 2 * level * randint(1, 6)
        self.dp = level / 2 * randint(1, 6)
        self.sp = level * randint(1, 6)
        self.img = "skeleton"

    def next_level(self):
        super().next_level()

