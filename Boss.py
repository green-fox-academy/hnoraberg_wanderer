from random import randint
from Enemy import Enemy

class Boss(Enemy):

    def __init__(self, x, y, level=1):
        super().__init__(x, y, level)
        self.x = x
        self.y = y
        self.name = "boss"
        self.hp = 2 * level * randint(1, 6) + randint(1, 6)
        self.dp = level/2 * randint(1, 6) + randint(1, 6) / 2
        self.sp = level * randint(1, 6) + level
        self.img = "boss"

    def next_level(self):
        super().next_level()
