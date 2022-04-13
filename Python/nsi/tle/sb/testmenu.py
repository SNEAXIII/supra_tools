import pygame
from pygame.locals import *
from menu import Menu

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((1080,720))
font = pygame.font.SysFont('Linux Biolinum G',55)
#text = smallfont.render('JOUER' , True , (0, 0, 0))

## Menu
run = True
menu = Menu(surface,font)

while run:
    surface.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN :
            menu.souris = True
        else :
            menu.souris = False

        if event.type == QUIT or menu.end :
            run = False
    menu.verif_bouton()
    menu.change_texture_bouton()
    menu.affiche_bouton()
    menu.affiche_texte()
    menu.click()
    pygame.display.flip()
    fpsClock.tick(60)

pygame.quit()
