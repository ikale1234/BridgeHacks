import pygame
import choose_picture


class Image:
    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.rad = 40

        self.visible = True
        self.path, self.index = choose_picture.getPic()
        self.image = pygame.image.load(self.path)

    def draw(self, win):
        if self.visible:
            win.blit(self.image, (self.x, self.y))
