import pygame
from sons import son_jeu
from barre import barre
from balls import balle
from bricks import bricks
from pygame.locals import *
from menu import Menu, Menu_Level, Niveau
from niveaux import liste_level_0

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
        self.font = pygame.font.SysFont('Linux Biolinum G', 55)
        self.Son_Jeu = son_jeu()
        self.menu = Menu(self.surface, self.font, souris())
        self.menu_niveau = Menu_Level(self.surface, self.font, souris())
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

    def add_ball(self, valeur):
        self.balls.add(
            balle(self.largeur_ecran, self.hauteur_ecran, self.Barre, self.Bricks, self.surface, self.Son_Jeu,
                  valeur.angle, valeur.vitesse))

    def partie(self, valeur):
        hp = valeur.hp_ball
        self.Bricks = bricks(self.surface, valeur.hp_brique, valeur.pattern)
        self.Barre = barre(self.surface)
        self.add_ball(valeur)
        en_vie = True
        while en_vie and self.run:
            self.Barre.tp_souris()

            for event in pygame.event.get():
                if event.type == QUIT:
                    en_vie = False
                    self.run = False

            self.Bricks.dessine_moi()

            for ball in self.balls:
                morts = False
                if ball.mort:
                    morts = ball
                else:
                    ball.colibrique()
                    ball.deplacement()
            if morts:
                self.balls.discard(morts)
            self.Barre.affiche()

            if self.balls == set():
                hp -= 1
                if hp >= 0:
                    self.add_ball(valeur)
                else:
                    en_vie = False

            self.frame()
        self.reset()

    def menu_principal(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    self.menu.souris.press = True
                else:
                    self.menu.souris.press = False
                if event.type == QUIT or self.menu.end:
                    self.run = False
            if self.menu.jeu:
                self.partie(Niveau(liste_level_0, 7, -2, 45, 1, 0))
                self.menu.reset()
            if self.menu.level:
                self.menu_level()
                self.menu_niveau.reset()
                self.menu.reset()

            self.menu.next_frame()
            self.frame()

    def menu_level(self):
        en_cours = True
        valeur = False
        while en_cours and self.run:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    self.menu_niveau.souris.press = True
                else:
                    self.menu_niveau.souris.press = False
                if event.type == QUIT:
                    self.run = False
                    en_cours = False

            if self.menu_niveau.end:
                en_cours = False

            if not valeur == False:
                self.partie(valeur)
                self.menu_niveau.reset()

            self.menu_niveau.next_frame()
            valeur = self.menu_niveau.click()
            self.frame()
