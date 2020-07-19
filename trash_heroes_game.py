import pygame
import random
from label_class import Label
from item_class import Image
from can_class import Can
win = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Where do I throw it?")
pygame.init()


class Game:
    def __init__(self):
        self.run = True
        self.item_list = []

        self.points = 0
        self.stage = 0
        self.mouse_down = 0

    # label variables
        self.game_label = Label("Trash Heroes", 32,
                                (0, 0, 0), (255, 255, 255), 500, 200)
        self.instructions_label = Label("Instructions", 20,
                                        (0, 0, 0), (255, 255, 255), 500, 450)
        self.play_label = Label("Play Game", 20,
                                (0, 0, 0), (255, 255, 255), 500, 650)
        self.the_instructions = Label("The Instructions", 32,
                                      (0, 0, 0), (255, 255, 255), 500, 200)

        self.sentence1 = Label("The objective is to catch the falling items in the correct bin.", 20,
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
        self.bg_color = (255, 255, 255)
        self.music = pygame.mixer.music.load("sound.mp3")
        pygame.mixer.music.play(-1)
        self.wrongsound = pygame.mixer.Sound("wrong.wav")
        self.rightsound = pygame.mixer.Sound("correct.wav")

    # item creation
        for i in range(30):
            self.item_list.append(
                Image(random.randrange(35, 885), -200 - 500*i))
        self.can = Can()
        self.hitcan = self.item_list[0]

    def drawgame(self):
        for item in self.item_list:
            item.draw(win)
        self.can.draw(win)
        self.score.changetext("Score: "+str(self.points))
        self.score.draw(win)
        pygame.display.update()

    def correct(self):
        self.points += 1
        self.score.changecolor((0, 255, 0))
        self.rightsound.play()

    def wrong(self):
        self.score.changecolor((255, 0, 0))
        self.wrongsound.play()

    def rungame(self):
        while self.run:
            win.fill(self.bg_color)
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.key = pygame.key.get_pressed()
            self.x, self.y = pygame.mouse.get_pos()

            if self.stage == 0:
                pygame.event.get()
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.mouse_down = 0
                if pygame.mouse.get_pressed() == (1, 0, 0) and self.mouse_down == 0:
                    if self.instructions_label.in_rect:
                        self.stage = 2
                        self.instructions_label.in_rect = False
                    elif self.play_label.in_rect:
                        self.stage = 1
                        self.play_again.in_rect = False
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
                    if self.play_label.in_rect:
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
                    if item.y + 40 > 700 and item.y + 40 < 750 and item.visible:
                        if item.x > self.can.x and item.x < self.can.x + 170:
                            item.visible = False
                            self.hitcan = item
                            if self.can.form == "trash":
                                if item.index == 0:
                                    self.correct()
                                else:
                                    self.wrong()
                            if self.can.form == "recycle":
                                if item.index == 1:
                                    self.correct()
                                else:
                                    self.wrong()
                            if self.can.form == "garden":
                                if item.index == 2:
                                    self.correct()
                                else:
                                    self.wrong()
                    if self.hitcan.y > 900:
                        self.score.changecolor((0, 0, 0))
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
                    if self.play_again.in_rect:
                        self.stage = 1
                        self.item_list = []
                        for i in range(30):
                            self.item_list.append(
                                Image(random.randrange(35, 885), -200 - 500*i))
                        self.can.change("trash")
                        self.points = 0
                        self.play_again.in_rect = False
                    elif self.back_to_start.in_rect:
                        self.stage = 0
                        self.item_list = []
                        for i in range(30):
                            self.item_list.append(
                                Image(random.randrange(35, 885), -200 - 500*i))
                        self.can.change("trash")
                        self.points = 0
                        self.mouse_down = 1
                        self.back_to_start.in_rect = False
                self.play_again.checkcursor(self.x, self.y, (0, 0, 255))
                self.back_to_start.checkcursor(self.x, self.y, (0, 0, 255))
                self.final_score.draw(win)
                self.play_again.draw(win)
                self.back_to_start.draw(win)
                pygame.display.update()
        quit()


game = Game()
game.rungame()
