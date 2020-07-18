import pygame
import random

win = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Osu")
pygame.init()
run = True
item_list = []
trashcan = pygame.image.load('trashcan.png')
recyclebin = pygame.image.load('recycle.png')
points = 0
colorchoices = [(255, 0, 0), (0, 0, 255)]
stage = 0

# label variables


class Label:
    def __init__(self, text, size, color, bgcolor, x, y):
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont('arial', size)
        self.label = self.font.render(self.text, True, color, bgcolor)
        self.rect = self.label.get_rect()
        self.rect.center = (x, y)


game_text = "Where Do I Throw It?"
font = pygame.font.SysFont('arial', 32)
game_label = font.render(game_text, True, (0, 0, 255), (255, 0, 0))
labelRect = game_label.get_rect()
labelRect.center = (500, 200)
stage = 0


class circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rad = 40

        self.vis = True
        self.color = random.choice(colorchoices)
        if self.color == colorchoices[0]:
            self.index = 0
        else:
            self.index = 1

    def draw(self, win):
        if self.vis:
            pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)


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
for i in range(30):
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
    if stage == 0:
        win.blit(game_label, labelRect)
        pygame.display.update()
    if stage == 1:
        # movement
        if key[pygame.K_LEFT]:
            can.x -= 10
        if key[pygame.K_RIGHT]:
            can.x += 10
    # bin switch
        if key[pygame.K_q]:
            can.change("trash")
        if key[pygame.K_w]:
            can.change("recycle")
        if key[pygame.K_e]:
            can.change("garden")
    # can touch conditions
        for item in item_list:
            if item.y > 670 and item.y < 730 and item.vis:
                if item.x > can.x + 40 and item.x < can.x + 210:
                    item.vis = False
                    if can.form == "trash":
                        if item.index == 0:
                            points += 1
                    if can.form == "recycle":
                        if item.index == 1:
                            points += 1
                    print(points)
        for item in item_list:
            item.y += 5
        drawgame()
quit()
