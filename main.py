from tkinter import *
from random import randint
from Map import Map
from Hero import Hero
from Skeleton import Skeleton
from Boss import Boss


IMG_SIZE = 52
WIDTH = 10 * IMG_SIZE
HEIGHT = (10 * IMG_SIZE) + IMG_SIZE

root = Tk()
root.title('Wanderer Game')
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

hero = Hero()
game_map = Map()
skeleton1 = Skeleton(6, 1, True)
skeleton2 = Skeleton(2, 6)
skeleton3 = Skeleton(8, 1)
boss = Boss(9, 1)
enemies = [skeleton1, skeleton2, skeleton3, boss]


def draw_screen():
    canvas.delete("all")
    for i in range(len(game_map.tiles)):
        for j in range(len(game_map.tiles[i])):
            if game_map.tiles[i][j] == 0:
                image = root.floor
            else:
                image = root.wall
            canvas.create_image(j * IMG_SIZE, i * IMG_SIZE, anchor=NW, image=image)
    if skeleton1.hp > 0:
        canvas.create_image(skeleton1.x * IMG_SIZE, skeleton1.y, image=root.skeleton, anchor=NW)
    elif skeleton1.hp <= 0:
        pass
    if skeleton2.hp > 0:
        canvas.create_image(skeleton2.x * IMG_SIZE, skeleton2.y, image=root.skeleton, anchor=NW)
    elif skeleton2.hp <= 0:
        pass
    if skeleton3.hp > 0:
        canvas.create_image(skeleton3.x * IMG_SIZE, skeleton3.y, image=root.skeleton, anchor=NW)
    elif skeleton3.hp <= 0:
        pass
    if boss.hp > 0:
        canvas.create_image(boss.x * IMG_SIZE, boss.y, image=root.boss, anchor=NW)
    elif boss.hp <= 0:
        pass
    canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE, image=getattr(root, hero.img), anchor=NW)
    label = Label(root, text=f"Hero (Level {hero.level}) HP: {hero.hp}/{hero.maxHp} | DP: {hero.dp} | SP: {hero.sp}")
    label.place(bordermode="inside", x=10, y=530)



def load_images():
    dir = "images/"
    root.floor = PhotoImage(file=dir + "floor.png")
    root.wall = PhotoImage(file=dir + "wall.png")
    root.hero_down = PhotoImage(file=dir + "hero-down.png")
    root.hero_up = PhotoImage(file=dir + "hero-up.png")
    root.hero_right = PhotoImage(file=dir + "hero-right.png")
    root.hero_left = PhotoImage(file=dir + "hero-left.png")
    root.skeleton = PhotoImage(file=dir + "skeleton.png")
    root.boss = PhotoImage(file=dir + "boss.png")

load_images()



def leftKey(event):
    hero.img = "hero_left"
    if game_map.is_floor(hero.x - 1, hero.y) and hero.x > 0:
        hero.move(x=-1)

def rightKey(event):
    hero.img = "hero_right"
    if game_map.is_floor(hero.x + 1, hero.y) and hero.x < 11:
        hero.move(x=+1)

def upKey(event):
    hero.img = "hero_up"
    if game_map.is_floor(hero.x, hero.y - 1) and hero.y > 0:
        hero.move(y=-1)

def downKey(event):
    hero.img = "hero_down"
    if game_map.is_floor(hero.x, hero.y + 1) and hero.y < 11:
        hero.move(y=1)

def spaceKey(event):
    for enemy in enemies:
        if hero.x == enemy.x and hero.y == enemy.y:
            strike_value = hero.sp + randint(1, 6)
            if ((2 * randint(1, 6) + hero.sp)) > enemy.dp:
                enemy.hp -= strike_value - enemy.dp
                if enemy.hp > 0 and hero.hp > 0:
                    hero.hp -= strike_value - hero.dp
                elif enemy.hp <= 0:
                    label_dead_enemy = Label(root, text="You killed the " + enemy.name + "      ")
                    label_dead_enemy.place(bordermode="inside", x=10, y=IMG_SIZE * 10 + 25)
                    if enemy.is_keyholder is True and boss.hp <= 0:
                        hero.level_up()
                        hero.enter_next_area()
                        enemy.next_level()
                elif hero.hp <= 0:
                    label_dead_hero = Label(root, text="You died.         ")
                    label_dead_hero.place(bordermode="inside", x=10, y=IMG_SIZE*10+25)



root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)
root.bind('<space>', spaceKey)



while True:
    draw_screen()
    root.update_idletasks()
    root.update()
