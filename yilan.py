import pygame, time, random

import sys
import os
##
##def resource_path(relative_path):
##    """ Get absolute path to resource, works for dev and for PyInstaller """
##    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
##    return os.path.join(base_path, relative_path)


pygame.init()
pencere_x, pencere_y = 600,400
pencere = pygame.display.set_mode((pencere_x,pencere_y))
siyah, beyaz, yesil, kirmizi = (0,0,0), (255,255,255), (0,150,0),(255,0,0)
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
yem_boy = yilan_boy = 20
elma_icon = pygame.image.load("elma.png")
pygame.display.set_icon(pygame.image.load("elma.png"))
font = pygame.font.SysFont("Arial",25)
font2 = pygame.font.SysFont("Arial",50)


def mesaj(msg,color,x,y):
    text = font.render(msg,True,color)
    pencere.blit(text,[x,y])
def mesaj2(mesaj,color,x,y):
    text2 = font2.render(mesaj,True,color)
    pencere.blit(text2,[x,y])
    pygame.display.update()
    time.sleep(1)
def yilan(yilan_boy,blok_list):
    for XveY in blok_list:
        
        pygame.draw.rect(pencere,yesil,[XveY[0],XveY[1],yilan_boy,yilan_boy])

def elma(yem_x,yem_y):
    pencere.blit(elma_icon,(yem_x,yem_y))
def gameintro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        pencere.fill(beyaz)
        mesaj("Press R to start, Q to quit.",siyah,150,200)
        mesaj2("Snake Game",siyah,150,150)
        pygame.display.update()
        clock.tick(5)

def gameloop():
    cikis = False
    bitti = False
    skor = 0
    yem_x = round(random.randrange(0,pencere_x-yem_boy,20))
    yem_y = round(random.randrange(0,pencere_y-yem_boy,20))
    yilan_x = pencere_x/2
    yilan_y = pencere_y/2
    yilan_x_mov = 0
    yilan_y_mov = 0
    blok_list = []
    yilan_uzunluk = 1
    while not cikis:
        while bitti == True:
            pencere.fill(siyah)
            mesaj("Press R to play, Q to quit.",beyaz,150,200)
            mesaj("Score: ",beyaz,150,220)
            mesaj(str(skor),beyaz,210,220)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cikis = True
                    bitti = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        cikis = True
                        bitti = False
                    if event.key == pygame.K_r:
                        gameloop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cikis = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    yilan_y_mov = -yilan_boy
                    yilan_x_mov = 0
                elif event.key == pygame.K_DOWN:
                    yilan_y_mov = +yilan_boy
                    yilan_x_mov = 0
                elif event.key == pygame.K_RIGHT:
                    yilan_x_mov = +yilan_boy
                    yilan_y_mov = 0
                elif event.key == pygame.K_LEFT:
                    yilan_x_mov = -yilan_boy
                    yilan_y_mov = 0

        if yem_x == yilan_x and yem_y == yilan_y:

            yem_x = round(random.randrange(0,pencere_x-yem_boy,20))
            yem_y = round(random.randrange(0,pencere_y-yem_boy,20))
            for i in blok_list:
                if i[0] == yem_x and i[1] == yem_y:
                    yem_x = round(random.randrange(0,pencere_x-yem_boy,20))
                    yem_y = round(random.randrange(0,pencere_y-yem_boy,20))
            skor += 1
            yilan_uzunluk += 1

        if yilan_x < 0  or yilan_x + yilan_boy > pencere_x or yilan_y < 0  or yilan_y + yilan_boy > pencere_y:
            bitti = True

        yilan_x += yilan_x_mov
        yilan_y += yilan_y_mov
        pencere.fill(beyaz)
        elma(yem_x,yem_y)


        yilan_bas = []
        yilan_bas.append(yilan_x)
        yilan_bas.append(yilan_y)
        blok_list.append(yilan_bas)
        yilan(yilan_boy,blok_list)
        if len(blok_list) > yilan_uzunluk:
            del blok_list[0]

        for vucut in blok_list[:-1]:
            if vucut == yilan_bas:
                bitti = True


        mesaj("Score:",siyah,420,20)
        mesaj(str(skor),siyah,470,20)
        pygame.display.update()
        clock.tick(15)



    pygame.quit()
    quit()

gameintro()
gameloop()
