import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")
wrong = pygame.mixer.Sound("wrong.wav")
right = pygame.mixer.Sound("correct.wav")
music = pygame.mixer.music.load("sound.mp3")
pygame.mixer.music.play(-1)
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        wrong.play()

    if keys[pygame.K_RIGHT]:
        right.play()
