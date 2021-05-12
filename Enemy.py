from random import randint

class Enemy:

    def __init__(self, x, y, level=1, is_keyholder=False):
        self.x = x
        self.y = y
        self.is_keyholder = is_keyholder
        self.level = level

    def next_level(self):
        self.hp = 2 * self.level * randint(1, 6)
        self.dp = self.level / 2 * randint(1, 6)
        self.sp = self.level * randint(1, 6)
        return self.hp, self.dp, self.sp

