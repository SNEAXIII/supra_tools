import pygame
from sons import son_jeu
from barre import barre
from balls import balle
from bricks import bricks
from pygame.locals import *
from menu import Menu

"""
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
"""

class souris:
    def __init__(self):
        self.press = False
        self.position()

    def position(self):
        self.pos = pygame.mouse.get_pos()

class jeu:
    def __init__(self):
        self.run = True
        self.fps = 60
        self.fond_ecran = (255, 255, 255)
        self.fpsClock = pygame.time.Clock()
        self.largeur_ecran = 1080
        self.hauteur_ecran = 720
        self.surface = pygame.display.set_mode((self.largeur_ecran, self.hauteur_ecran))
        self.angle_base = 45
        self.font = pygame.font.SysFont('Linux Biolinum G',55)
        self.Son_Jeu = son_jeu()
        self.menu = Menu(self.surface,self.font,souris())
        self.reset()

    def reset(self):
        self.Bricks = None
        self.Barre = None
        self.balls = set()

    def frame(self):
        self.Son_Jeu.joue()
        pygame.display.flip()
        self.fpsClock.tick(self.fps)
        self.surface.fill(self.fond_ecran)

    def add_ball(self):
        self.balls.add(
            balle(self.largeur_ecran, self.hauteur_ecran, self.Barre, self.Bricks, self.surface, self.Son_Jeu,
                  self.angle_base, 10))

    def partie(self):
        hp = 3
        self.Bricks = bricks(self.surface)
        self.Barre = barre(self.surface)
        self.add_ball()
        en_vie = True
        while en_vie:
            self.Barre.tp_souris()

            for event in pygame.event.get():
                if event.type == QUIT:
                    en_vie = False
                    self.run = False

            self.Bricks.dessine_moi()

            for ball in self.balls:
                morts = False
                if ball.mort: morts = ball
                else:
                    ball.colibrique()
                    ball.deplacement()
            if morts: self.balls.discard(morts)
            if self.balls == set():
                hp -= 1
                if hp >= 0:
                    self.add_ball()
                else:
                    en_vie = False
            self.Barre.affiche()


            self.frame()
        self.reset()

    def menu_principal(self):
        en_cours = True
        while en_cours:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    self.menu.souris.press = True
                else:
                    self.menu.souris.press = False
                if event.type == QUIT or self.menu.end:
                    self.run = False
                    en_cours = False
                if self.menu.jeu:
                    self.partie()
                    self.menu.reset()
                if self.menu.level:
                    # level_
                    pass
            self.menu.souris.position()
            self.menu.verif_bouton()
            self.menu.change_texture_bouton()
            self.menu.affiche_bouton()
            self.menu.affiche_texte()
            self.menu.click()
            self.frame()

