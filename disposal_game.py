import pygame
import random

win = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Osu")
run = True
item_list = []
trashcan = pygame.image.load('trashcan.png')
recyclebin = pygame.image.load('recycle.png')
points = 0


class circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rad = 40

        self.vis = True

    def draw(self, win):
        if self.vis:
            pygame.draw.circle(win, (0, 0, 255), (self.x, self.y), self.rad)


class Can:
    def __init__(self):
        self.x = 400
        self.y = 700
        self.form = "trash"

    def draw(self, win):
        if self.form == "trash":
            win.blit(trashcan, (self.x, self.y))
        elif self.form == "recycle":
            win.blit(recyclebin, (self.x, self.y))

    def change(self, form):
        self.form = form


# item creation
for i in range(10):
    item_list.append(circle(random.randrange(75, 925), -200 - 500*i))
can = Can()


def drawgame():
    for item in item_list:
        item.draw(win)
    can.draw(win)
    pygame.display.update()


while run:
    win.fill((255, 255, 255))
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

# movement
    if key[pygame.K_LEFT]:
        can.x -= 10
    if key[pygame.K_RIGHT]:
        can.x += 10
# can touch conditions
    for item in item_list:
        if item.y > 670 and item.y < 730 and item.vis:
            if item.x > can.x + 40 and item.x < can.x + 210:
                item.vis = False
                points += 1
                print(points)
    for item in item_list:
        item.y += 5
    drawgame()
quit()
