import pygame
import random
pygame.init()

dim = 3
win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Tic Tac Toe")
run = True
box = []
for i in range(dim):
    box.append([])
    for j in range(dim):
        box[i].append(0)

symbol = "X"

dis = 400/dim
end = False
what = "c"
draw = False
movemade = False
def checkxy(bx, xmin, xmax, ymin, ymax):
    global x,y,symbol,end,movemade
    if bx == 0 and end == False:
        if x > xmin and x < xmax:
            if y > ymin and y < ymax:
                if symbol == "X":
                    bx = 1
                    symbol = "O"
                elif symbol == "O":
                    bx = 2
                    symbol = "X"
                movemade = True
    return bx
def drawx(x1,y1):
    pygame.draw.line(win, (0,0,255), (x1+10,y1+10), (x1+dis-17,y1+dis-17), 5)
    pygame.draw.line(win, (0,0,255), (x1+10,y1+dis-17), (x1+dis-17,y1+10), 5)
def drawo(xr,yr):
    pygame.draw.circle(win, (0,255,0), (xr,yr), int(170/dim), 3)



while run:
    win.fill((0,0,0))
    pygame.time.delay(10)
    x,y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if end ==False:
                for i in range(dim):
                    for j in range(dim):
                        box[i][j] = checkxy(box[i][j],(200+(j*400)/dim), (200+((j+1)*400)/dim), (200+(i*400)/dim), (200+((i+1)*400)/dim))

    for i in range(len(box)):
        for j in range(len(box[i])):
            if box[i][j]==1:

                if i == 0:
                    y1 = (200+(i*400)/dim)
                else:
                    y1 = (200+(i*400)/dim)+3
                if j == 0:
                    x1 = (200+(j*400)/dim)
                else:
                    x1 = (200+(j*400)/dim)+3

                drawx(x1,y1)
            if box[i][j]==2:

                x2 = int(((200+(j*400)/dim)+(200+((j+1)*400)/dim))/2)

                y2 = int(((200+(i*400)/dim)+(200+((i+1)*400)/dim))/2)
                drawo(x2,y2)

    if movemade == True:
        right = 0
        for i in range(len(box)):
            for j in range(len(box[i])):
                if i == j:
                    if box[i][j] == 1:
                        right += 1
                    if right == dim:
                        end = True

        right = 0
        for i in range(len(box)):
            for j in range(len(box[i])):
                if i == j:
                    if box[i][j] == 2:
                        right += 1
                    if right == dim:
                        end = True

        right = 0
        for i in range(len(box)):
            for j in range(len(box[i])):
                if i == (dim-1)-j:
                    if box[i][j] == 1:
                        right += 1
                    if right == dim:
                        end = True

        right = 0
        for i in range(len(box)):
            for j in range(len(box[i])):
                if i == (dim-1)-j:
                    if box[i][j] == 2:
                        right += 1
                    if right == dim:
                        end = True

        for i in range(len(box)):
            count = 0
            i1 = 0
            for j in range(len(box[i])):
                count +=1
                if count == 1 and box[i][j] != 0:
                    i1 = box[i][j]
                if i1 != 0:
                    if box[i][j] != i1:
                        break
                    if count == dim:
                        end = True

        for j in range(len(box)):
            count = 0
            i1 = 0
            for i in range(len(box[j])):
                count +=1
                if count == 1 and box[i][j] != 0:
                    i1 = box[i][j]
                if i1 != 0:
                    if box[i][j] != i1:
                        break
                    if count == dim:
                        end = True

        draw = True
        if end == False:
            for i in range(len(box)):
                for j in range(len(box[i])):
                    if box[i][j] == 0:
                        draw = False
    movemade = False

    if draw == True or end == True:
        if symbol == "X":
            what = "O"
        if symbol == "O":
            what = "X"
        if end != True:
            what = "Nobody"
        who = what+" wins."
    else:
        who = "It is "+symbol+"\'s turn."


    font = pygame.font.SysFont("Times New Roman", 30)
    turn = font.render(who,True, (255,255,255))
    win.blit(turn, (400-turn.get_rect().width/2,100))

    for i in range(dim-1):
        pygame.draw.rect(win, (255,0,0), (200, int((200+((i+1)*400)/dim)-3), 400, 6))
        pygame.draw.rect(win, (255,0,0), (int((200+((i+1)*400)/dim)-3), 200, 6, 400))

    pygame.display.update()
pygame.quit()
