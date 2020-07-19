import pygame
import random
import os
import randompictest
win = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Where do I throw it?")
pygame.init()


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


class image:
    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.rad = 40

        self.vis = True
        self.path, self.index = randompictest.getPic()
        self.image = pygame.image.load(self.path)

    def draw(self, win):
        if self.vis:
            win.blit(self.image, (self.x, self.y))


class Can:
    def __init__(self):
        self.x = 400
        self.y = 700
        self.form = "trash"
        self.trashcan = pygame.image.load('trashcan.png')
        self.recyclebin = pygame.image.load('recycle.png')
        self.yardtrimmings = pygame.image.load('yard.png')

    def draw(self, win):
        if self.form == "trash":
            win.blit(self.trashcan, (self.x, self.y))
        elif self.form == "recycle":
            win.blit(self.recyclebin, (self.x, self.y))
        elif self.form == "garden":
            win.blit(self.yardtrimmings, (self.x, self.y))

    def change(self, form):
        self.form = form


class Game:
    def __init__(self):
        self.run = True
        self.item_list = []

        self.points = 0
        self.stage = 0
        self.mousedown = 0

    # label variables
        self.game_label = Label("Where Do I Throw It?", 32,
                                (0, 0, 0), (255, 255, 255), 500, 200)
        self.instructions_label = Label("Instructions", 20,
                                        (0, 0, 0), (255, 255, 255), 500, 450)
        self.play_label = Label("Play Game", 20,
                                (0, 0, 0), (255, 255, 255), 500, 650)
        self.the_instructions = Label("The Instructions", 32,
                                      (0, 0, 0), (255, 255, 255), 500, 200)

        self.sentence1 = Label("The objective is to catch the falling items in the correct bin", 20,
                               (0, 0, 0), (255, 255, 255), 500, 350)
        self.sentence2 = Label("You can move the bin with the right and left arrows.", 20,
                               (0, 0, 0), (255, 255, 255), 500, 425)
        self.sentence3 = Label("You can switch bins with these keybinds: 1 = Trash Can, 2 = Recycling Bin, 3 = Yard Trimmings Bin.", 20,
                               (0, 0, 0), (255, 255, 255), 500, 500)
        self.stage = 0

        self.score = Label("Score: "+str(self.points), 32,
                           (0, 0, 0), (255, 255, 255), 500, 50)

        self.play_again = Label("Play Again", 20,
                                (0, 0, 0), (255, 255, 255), 500, 600)
        self.final_score = Label("Your Final Score", 32, (0, 0, 0),
                                 (255, 255, 255), 500, 250)

        self.back_to_start = Label("Return to Title Screen", 20,
                                   (0, 0, 0), (255, 255, 255), 500, 700)
        self.bgcolor = (255, 255, 255)

    # item creation
        for i in range(30):
            self.item_list.append(
                image(random.randrange(35, 885), -200 - 500*i))
        self.can = Can()

    def drawgame(self):
        for item in self.item_list:
            item.draw(win)
        self.can.draw(win)
        self.score.changetext("Score: "+str(self.points))
        self.score.draw(win)
        pygame.display.update()

    def rungame(self):
        while self.run:
            win.fill(self.bgcolor)
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.key = pygame.key.get_pressed()
            self.x, self.y = pygame.mouse.get_pos()

            if self.stage == 0:
                pygame.event.get()
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.mousedown = 0
                if pygame.mouse.get_pressed() == (1, 0, 0) and self.mousedown == 0:
                    if self.instructions_label.inrect:
                        self.stage = 2
                        self.instructions_label.inrect = False
                    elif self.play_label.inrect:
                        self.stage = 1
                        self.play_again.inrect = False
                self.instructions_label.checkcursor(
                    self.x, self.y, (0, 0, 255))
                self.play_label.checkcursor(self.x, self.y, (0, 0, 255))
                self.game_label.draw(win)
                self.instructions_label.draw(win)
                self.play_label.draw(win)
                pygame.display.update()

            if self.stage == 2:
                pygame.event.get()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if self.play_label.inrect:
                        self.stage = 1
                self.play_label.checkcursor(self.x, self.y, (0, 0, 255))
                self.the_instructions.draw(win)
                self.sentence1.draw(win)
                self.sentence2.draw(win)
                self.sentence3.draw(win)
                self.play_label.draw(win)
                pygame.display.update()

            if self.stage == 1:
                # movement
                if self.key[pygame.K_LEFT]:
                    self.can.x -= 10
                if self.key[pygame.K_RIGHT]:
                    self.can.x += 10
            # bin switch
                if self.key[pygame.K_1]:
                    self.can.change("trash")
                if self.key[pygame.K_2]:
                    self.can.change("recycle")
                if self.key[pygame.K_3]:
                    self.can.change("garden")
            # can touch conditions
                for item in self.item_list:
                    if item.y + 40 > 700 and item.y + 40 < 750 and item.vis:
                        if item.x > self.can.x and item.x < self.can.x + 170:
                            item.vis = False
                            if self.can.form == "trash":
                                if item.index == 0:
                                    self.points += 1
                                    right = pygame.mixer.music.load(
                                        "correct.mp3")
                                else:
                                    wrong = pygame.mixer.music.load(
                                        "wrong.mp3")
                            if self.can.form == "recycle":
                                if item.index == 1:
                                    self.points += 1
                                    right = pygame.mixer.music.load(
                                        "correct.mp3")
                                else:
                                    wrong = pygame.mixer.music.load(
                                        "wrong.mp3")
                            if self.can.form == "garden":
                                if item.index == 2:
                                    self.points += 1
                                    right = pygame.mixer.music.load(
                                        "correct.mp3")
                                else:
                                    wrong = pygame.mixer.music.load(
                                        "wrong.mp3")
                            pygame.mixer.music.play()
            # difficulty increasing with skill

                if self.item_list[5].y < 1000:
                    self.speed = 2
                if self.item_list[5].y > 1000 and self.item_list[5].y < 1100:
                    if self.points > 3:
                        self.speed = 3
                if self.item_list[10].y > 1000 and self.item_list[10].y < 1100:
                    if self.points > 7:
                        self.speed = 4
                if self.item_list[15].y > 1000 and self.item_list[15].y < 1100:
                    if self.points > 12:
                        self.speed = 5
                if self.item_list[20].y > 1000 and self.item_list[20].y < 1100:
                    if self.points > 17:
                        self.speed = 6

                for item in self.item_list:
                    item.y += self.speed
                if self.item_list[29].y > 1000:
                    self.stage = 3
                    self.final_score.changetext("Your final score was " +
                                                str(self.points) + " / " + str(len(self.item_list)) + ".")
                self.drawgame()
            if self.stage == 3:
                pygame.event.get()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if self.play_again.inrect:
                        self.stage = 1
                        self.item_list = []
                        for i in range(30):
                            self.item_list.append(
                                image(random.randrange(35, 885), -200 - 500*i))
                        self.can.change("trash")
                        self.points = 0
                        self.play_again.inrect = False
                    elif self.back_to_start.inrect:
                        self.stage = 0
                        self.item_list = []
                        for i in range(30):
                            self.item_list.append(
                                image(random.randrange(35, 885), -200 - 500*i))
                        self.can.change("trash")
                        self.points = 0
                        self.mousedown = 1
                        self.back_to_start.inrect = False
                self.play_again.checkcursor(self.x, self.y, (0, 0, 255))
                self.back_to_start.checkcursor(self.x, self.y, (0, 0, 255))
                self.final_score.draw(win)
                self.play_again.draw(win)
                self.back_to_start.draw(win)
                pygame.display.update()
        quit()


game = Game()
game.rungame()
