import pygame
from sons import son_jeu
from barre import barre
from balls import balle
from bricks import bricks
from pygame.locals import *

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

# Boucle du jeu
Son_Jeu = son_jeu()
print(Bricks)
morts = False
while run:
    surface.fill((255, 255, 255))
    # permet de déplacer la barre en suivant la souris
    Barre.tp_souris()

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == MOUSEBUTTONDOWN :
            click = True

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
        balls.add(balle(largeur, hauteur, Barre,Bricks,surface,Son_Jeu, angle_base, 5))
    # On créé un rectangle coloré pour la base de la barre
    pygame.draw.rect(surface, coul_barre, pygame.Rect(Barre.x - Barre.taille_x, Barre.y - Barre.taille_y, Barre.taille_x * 2, Barre.taille_y * 2))
    pygame.draw.rect(surface, noir, pygame.Rect(Barre.x - Barre.taille_x, Barre.y - Barre.taille_y, Barre.taille_x * 2, Barre.taille_y * 2), 1)
    Barre.placement_textu_teco()
    # On créé un contour de rectangle noir
    Son_Jeu.joue()
    pygame.display.flip()
    fpsClock.tick(60)

# fin de la boucle
pygame.quit()
