import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        wrong = pygame.mixer.music.load("wrong.mp3")
        pygame.mixer.music.play()

    if keys[pygame.K_RIGHT]:
        right = pygame.mixer.music.load("correct.mp3")
        pygame.mixer.music.play()
