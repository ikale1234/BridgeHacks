import pygame


class Can:
    def __init__(self):
        self.x = 400
        self.y = 700
        self.form = "trash"
        self.trash_can = pygame.image.load('trashcan.png')
        self.recycle_bin = pygame.image.load('recycle.png')
        self.yard_trimmings = pygame.image.load('yard.png')

    def draw(self, win):
        if self.form == "trash":
            win.blit(self.trash_can, (self.x, self.y))
        elif self.form == "recycle":
            win.blit(self.recycle_bin, (self.x, self.y))
        elif self.form == "garden":
            win.blit(self.yard_trimmings, (self.x, self.y))

    def change(self, form):
        self.form = form
