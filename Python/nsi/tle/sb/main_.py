import pygame
from sons import son_jeu
from barre import barre
from balls import balle
from bricks import bricks
from pygame.locals import *
from menu import Menu

# initialisation de la fenêtre Pygame
pygame.init()
run = True
fps = 60
fpsClock = pygame.time.Clock()
rouge = (255, 0, 0)
coul_barre = (237, 190, 82)
noir = (0, 0, 0)
largeur, hauteur = 1080, 720
surface = pygame.display.set_mode((largeur, hauteur))
# Définition des briques
Bricks = bricks(surface, r"textures\brick\blue_brick.png")
# Définition de la barre
Barre = barre(surface, (r"textures\stick\left_player_stick.png", r"textures\stick\right_player_stick.png"))
# Définition de la balle
balls = set()
angle_base = 45
click = False

font = pygame.font.SysFont('Linux Biolinum G',55)
menu = Menu(surface,font)

# Boucle du jeu
Son_Jeu = son_jeu()
print(Bricks)
morts = False
menu_ = True # lance le menu
jeu_ = False # lance le jeu
level_ = False # lance le menu des niveaux


while run:
    #partie generale
    surface.fill((255, 255, 255))

    #menu

    if menu_:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN : menu.souris = True
            else : menu.souris = False
            if event.type == QUIT or menu.end : run = False
            if menu.jeu:
                jeu_ = True
                menu_ = False
                balls.add(balle(largeur, hauteur, Barre,Bricks,surface,Son_Jeu, angle_base, 5))
                menu.reset()
            if menu.level:
                level_ = True
                menu_ = False
        menu.verif_bouton()
        menu.change_texture_bouton()
        menu.affiche_bouton()
        menu.affiche_texte()
        menu.click()

    # jeu
    if jeu_:

        Barre.tp_souris()

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

    # Update

    # Draw
        Bricks.dessine_moi()
        for ball in balls:
            morts = False
            if ball.mort: morts = ball
            else:
                #ball.Barre.x = ball.x
                ball.colibrique()
                ball.deplacement()
        if morts: balls.discard(morts)
        if balls == set():
            Bricks.reset_()
            jeu_ = False
            menu_ = True
    # On créé un rectangle coloré pour la base de la barre
        pygame.draw.rect(surface, coul_barre, pygame.Rect(Barre.x - Barre.taille_x, Barre.y - Barre.taille_y, Barre.taille_x * 2, Barre.taille_y * 2))
        pygame.draw.rect(surface, noir, pygame.Rect(Barre.x - Barre.taille_x, Barre.y - Barre.taille_y, Barre.taille_x * 2, Barre.taille_y * 2), 1)
        Barre.placement_textu_teco()
    # On créé un contour de rectangle noir



    #fin boucle
    Son_Jeu.joue()
    pygame.display.flip()
    fpsClock.tick(60)

    # niveaux
    if level_:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN : menu.souris = True
            else : level.souris = False
            if event.type == QUIT: run = False
            if level.level_1 :
                jeu_ = True
                menu_ = False
                balls.add(balle(largeur, hauteur, Barre, Bricks, surface, Son_Jeu, angle_base, 6))
                level.reset()
            if level.retour_menu :
                menu_ = True
                level_ = False
        level.verif_bouton() # problème ici au lancement -> fin du cours = pas le temps
        level.change_texture_bouton()
        level.affiche_bouton()
        level.affiche_texte()
        level.click()

# fin de la boucle
pygame.quit()

# Alexis