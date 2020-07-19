import pygame
import random
from label_class import Label
from item_class import Image
from can_class import Can


TITLE_STAGE = 0
GAME_STAGE = 1
INSTRUCTION_STAGE = 2
END_STAGE = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
width = 1000
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Where do I throw it?")
pygame.init()
width/2


class Game:
    def __init__(self):
        self.run = True
        self.item_list = []

        self.points = 0
        self.mouse_down = 0
        self.stage = TITLE_STAGE

        # label variables
        self.game_label = Label("Trash Heroes", 32,
                                BLACK, WHITE, width/2, 200)
        self.instructions_label = Label("Instructions", 20,
                                        BLACK, WHITE, width/2, 450)
        self.play_label = Label("Play Game", 20,
                                BLACK, WHITE, width/2, 650)
        self.the_instructions = Label("The Instructions", 32,
                                      BLACK, WHITE, width/2, 200)

        self.sentence1 = Label("The objective is to catch the falling items in the correct bin.", 20,
                               BLACK, WHITE, width/2, 350)
        self.sentence2 = Label("You can move the bin with the right and left arrows.", 20,
                               BLACK, WHITE, width/2, 425)
        self.sentence3 = Label("You can switch bins with these keybinds: 1 = Trash Can, 2 = Recycling Bin, 3 = Yard Trimmings Bin.", 20,
                               BLACK, WHITE, width/2, 500)

        self.score = Label("Score: "+str(self.points), 32,
                           BLACK, WHITE, width/2, 50)

        self.play_again = Label("Play Again", 20,
                                BLACK, WHITE, width/2, 600)
        self.final_score = Label("Your Final Score", 32, BLACK,
                                 WHITE, width/2, 250)

        self.back_to_start = Label("Return to Title Screen", 20,
                                   BLACK, WHITE, width/2, 700)
        self.bg_color = WHITE
        self.music = pygame.mixer.music.load("sound.mp3")
        pygame.mixer.music.play(-1)
        self.wrongsound = pygame.mixer.Sound("wrong.wav")
        self.rightsound = pygame.mixer.Sound("correct.wav")

        # Create items
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
        self.score.changecolor(GREEN)
        self.rightsound.play()

    def wrong(self):
        self.score.changecolor(RED)
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

            if self.stage == TITLE_STAGE:
                pygame.event.get()
                if pygame.mouse.get_pressed() == BLACK:
                    self.mouse_down = 0
                if pygame.mouse.get_pressed() == (1, 0, 0) and self.mouse_down == 0:
                    if self.instructions_label.in_rect:
                        self.stage = INSTRUCTION_STAGE
                        self.instructions_label.in_rect = False
                    elif self.play_label.in_rect:
                        self.stage = GAME_STAGE
                        self.play_again.in_rect = False
                self.instructions_label.checkcursor(
                    self.x, self.y, GRAY)
                self.play_label.checkcursor(self.x, self.y, GRAY)
                self.game_label.draw(win)
                self.instructions_label.draw(win)
                self.play_label.draw(win)
                pygame.display.update()

            if self.stage == INSTRUCTION_STAGE:
                pygame.event.get()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if self.play_label.in_rect:
                        self.stage = GAME_STAGE
                self.play_label.checkcursor(self.x, self.y, GRAY)
                self.the_instructions.draw(win)
                self.sentence1.draw(win)
                self.sentence2.draw(win)
                self.sentence3.draw(win)
                self.play_label.draw(win)
                pygame.display.update()

            if self.stage == GAME_STAGE:
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
                        self.score.changecolor(BLACK)

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
            if self.stage == END_STAGE:
                pygame.event.get()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if self.play_again.in_rect:
                        self.stage = GAME_STAGE
                        self.item_list = []
                        for i in range(30):
                            self.item_list.append(
                                Image(random.randrange(35, 885), -200 - 500*i))
                        self.can.change("trash")
                        self.points = 0
                        self.play_again.in_rect = False
                    elif self.back_to_start.in_rect:
                        self.stage = TITLE_STAGE
                        self.item_list = []
                        for i in range(30):
                            self.item_list.append(
                                Image(random.randrange(35, 885), -200 - 500*i))
                        self.can.change("trash")
                        self.points = 0
                        self.mouse_down = 1
                        self.back_to_start.in_rect = False
                self.play_again.checkcursor(self.x, self.y, GRAY)
                self.back_to_start.checkcursor(self.x, self.y, GRAY)
                self.final_score.draw(win)
                self.play_again.draw(win)
                self.back_to_start.draw(win)
                pygame.display.update()
        quit()


game = Game()
game.rungame()
