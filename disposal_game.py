import pygame
import random
import os
import randompictest


win = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Where do I throw it?")
pygame.init()
run = True
item_list = []
trashcan = pygame.image.load('trashcan.png')
recyclebin = pygame.image.load('recycle.png')
yardtrimmings = pygame.image.load('yard.png')
points = 0
colorchoices = [(255, 0, 0), (0, 0, 255)]
stage = 0
mousedown = 0


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

    def changetext(self, text):
        self.label = self.font.render(text, True, self.color, self.bgcolor)
        self.rect = self.label.get_rect()
        self.rect.center = (self.x, self.y)

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
sentence3 = Label("You can switch bins with these keybinds: 1 = Trash Can, 2 = Recycling Bin, 3 = Yard Trimmings Bin.", 20,
                  (0, 0, 0), (255, 255, 255), 500, 500)
stage = 0

score = Label("Score: "+str(points), 32, (0, 0, 0), (255, 255, 255), 500, 50)

play_again = Label("Play Again", 20,
                   (0, 0, 0), (255, 255, 255), 500, 600)
final_score = Label("Your Final Score", 32, (0, 0, 0),
                    (255, 255, 255), 500, 250)

back_to_start = Label("Return to Title Screen", 20,
                      (0, 0, 0), (255, 255, 255), 500, 700)

count = 0


class image:
    def __init__(self, x, y):
        global count
        self.x = x
        self.y = y

        self.rad = 40

        self.vis = True
        self.path, self.index = randompictest.getPic()
        print("hi", count)
        count += 1
        self.image = pygame.image.load(self.path)

    def draw(self, win):
        if self.vis:
            win.blit(self.image, (self.x, self.y))


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
        elif self.form == "garden":
            win.blit(yardtrimmings, (self.x, self.y))

    def change(self, form):
        self.form = form


# item creation
for i in range(30):
    item_list.append(image(random.randrange(35, 885), -200 - 500*i))
can = Can()


def drawgame():
    for item in item_list:
        item.draw(win)
    can.draw(win)
    score.changetext("Score: "+str(points))
    score.draw(win)
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
        if pygame.mouse.get_pressed() == (0, 0, 0):
            mousedown = 0
        if pygame.mouse.get_pressed() == (1, 0, 0) and mousedown == 0:
            if instructions_label.inrect:
                stage = 2
                instructions_label.inrect = False
            elif play_label.inrect:
                stage = 1
                play_again.inrect = False
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
        if key[pygame.K_1]:
            can.change("trash")
        if key[pygame.K_2]:
            can.change("recycle")
        if key[pygame.K_3]:
            can.change("garden")
    # can touch conditions
        for item in item_list:
            if item.y + 40 > 700 and item.y + 40 < 750 and item.vis:
                if item.x > can.x and item.x < can.x + 170:
                    item.vis = False
                    if can.form == "trash":
                        if item.index == 0:
                            points += 1
                    if can.form == "recycle":
                        if item.index == 1:
                            points += 1
                    if can.form == "garden":
                        if item.index == 2:
                            points += 1
        for item in item_list:
            item.y += 5
        if item_list[29].y > 1000:
            stage = 3
            final_score.changetext("Your final score was " +
                                   str(points) + " / " + str(len(item_list)) + ".")
        drawgame()
    if stage == 3:
        pygame.event.get()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if play_again.inrect:
                stage = 1
                item_list = []
                for i in range(30):
                    item_list.append(
                        image(random.randrange(35, 885), -200 - 500*i))
                can.change("trash")
                points = 0
                play_again.inrect = False
            elif back_to_start.inrect:
                stage = 0
                item_list = []
                for i in range(30):
                    item_list.append(
                        image(random.randrange(35, 885), -200 - 500*i))
                can.change("trash")
                points = 0
                mousedown = 1
                back_to_start.inrect = False
        play_again.checkcursor(x, y, (0, 0, 255))
        back_to_start.checkcursor(x, y, (0, 0, 255))
        final_score.draw(win)
        play_again.draw(win)
        back_to_start.draw(win)
        pygame.display.update()
quit()
