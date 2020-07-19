import pygame
import random
import os


def getPic():
    pictureDirectory = ["recycle", "trash", "yardtrim"]
    trashTypeNum = random.randrange(0, 3)
    trashType = os.listdir(pictureDirectory[trashTypeNum])
    randomPic = trashType[random.randrange(0, len(trashType))]
    path = os.path.join(pictureDirectory[trashTypeNum], randomPic)
    return path, trashTypeNum


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


class Label:
    def __init__(self, text, size, color, bgcolor, x, y):
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont('arial', size)
        self.color = color
        self.width, self.height = self.font.size(self.text)
        self.bgcolor = bgcolor
        self.label = self.font.render(self.text, True, color, self.bgcolor)
        self.rect = self.label.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        self.inrect = False

    def draw(self, win):
        win.blit(self.label, self.rect)

    def checkcursor(self, x, y, color):
        if x > self.x - self.width/2 and x < self.x + self.width/2:
            if y > self.y - self.height/2 and y < self.y + self.height/2:
                self.label = self.font.render(
                    self.text, True, self.color, color)
                self.inrect = True
            else:
                self.label = self.font.render(
                    self.text, True, self.color, self.bgcolor)
                self.inrect = False
        else:
            self.label = self.font.render(
                self.text, True, self.color, self.bgcolor)
            self.inrect = False

# label variables


game_label = Label("Where Do I Throw It?", 32,
                   (0, 0, 0), (255, 255, 255), 500, 200)
instructions_label = Label("Instructions", 20,
                           (0, 0, 0), (255, 255, 255), 500, 450)
play_label = Label("Play Game", 20,
                   (0, 0, 0), (255, 255, 255), 500, 650)
the_instructions = Label("The Instructions", 32,
                         (0, 0, 0), (255, 255, 255), 500, 200)

sentence1 = Label("The objective is to catch the falling items in the correct bin", 20,
                  (0, 0, 0), (255, 255, 255), 500, 350)
sentence2 = Label("You can move the bin with the right and left arrows.", 20,
                  (0, 0, 0), (255, 255, 255), 500, 425)
sentence3 = Label("You can switch bins with these keybinds: Q = Trash Can, W = Recycling Bin, E = Garden Scraps Bin.", 20,
                  (0, 0, 0), (255, 255, 255), 500, 500)
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
    x, y = pygame.mouse.get_pos()

    if stage == 0:
        pygame.event.get()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if instructions_label.inrect:
                stage = 2
            elif play_label.inrect:
                stage = 1
        instructions_label.checkcursor(x, y, (0, 0, 255))
        play_label.checkcursor(x, y, (0, 0, 255))
        game_label.draw(win)
        instructions_label.draw(win)
        play_label.draw(win)
        pygame.display.update()

    if stage == 2:
        pygame.event.get()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if play_label.inrect:
                stage = 1
        play_label.checkcursor(x, y, (0, 0, 255))
        the_instructions.draw(win)
        sentence1.draw(win)
        sentence2.draw(win)
        sentence3.draw(win)
        play_label.draw(win)
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
