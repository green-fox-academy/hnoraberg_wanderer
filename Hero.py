from random import randint

class Hero:

    def __init__(self, level=1):
        self.x = 0
        self.y = 0
        self.hp = 20 + 3 * randint(1, 6)
        self.dp = 2 * randint(1, 6)
        self.sp = 5 + randint(1, 6)
        self.maxHp = 38
        self.level = level
        self.img = "hero_down"

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def level_up(self):
        self.level += 1
        self.maxHp += randint(1, 6)
        self.dp += randint(1, 6)
        self.sp += randint(1, 6)
        self.x = self.__init__().x
        self.y = self.__init__().y
        return self.level, self.maxHp, self.dp, self.sp, self.x, self. y

    def enter_next_area(self):
        random_number = randint(1, 10)
        if random_number <= 5:
            self.hp += self.maxHp // 10
        elif random_number <= 9:
            self.hp += self.maxHp // 3
        else:
            self.hp = self.maxHp
        return self.hp


