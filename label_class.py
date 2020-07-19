import pygame


class Label:
    def __init__(self, text, size, color, bg_color, x, y):
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont('arial', size)
        self.color = color
        self.width, self.height = self.font.size(self.text)
        self.bg_color = bg_color
        self.label = self.font.render(self.text, True, color, self.bg_color)
        self.rect = self.label.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        self.in_rect = False

    def draw(self, win):
        win.blit(self.label, self.rect)

    def checkcursor(self, x, y, color):
        if x > self.x - self.width/2 and x < self.x + self.width/2:
            if y > self.y - self.height/2 and y < self.y + self.height/2:
                self.label = self.font.render(
                    self.text, True, self.color, color)
                self.in_rect = True
            else:
                self.label = self.font.render(
                    self.text, True, self.color, self.bg_color)
                self.in_rect = False
        else:
            self.label = self.font.render(
                self.text, True, self.color, self.bg_color)
            self.in_rect = False

    def changetext(self, text):
        self.label = self.font.render(text, True, self.color, self.bg_color)
        self.rect = self.label.get_rect()
        self.rect.center = (self.x, self.y)

    def changecolor(self, color):
        self.color = color
        self.label = self.font.render(
            self.text, True, self.color, self.bg_color)
