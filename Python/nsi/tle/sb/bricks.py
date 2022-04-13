import pygame

## Class Bricks
'''Création des briques dans la fenêtre du jeu'''
class bricks:

    def __init__(self, surface):
        self.img = {
            "blue" :pygame.image.load(r"textures\brick\blue_brick.png"),
            "green" :pygame.image.load(r"textures\brick\green_brick.png")
                    }
        self.fissures = {
            "fissure1" : pygame.image.load(r"textures\crack\layer_crack_phase1.png"),
            "fissure2" : pygame.image.load(r"textures\crack\layer_crack_phase2.png"),
            "fissure3" : pygame.image.load(r"textures\crack\layer_crack_phase3.png")
                    }
        self.surface = surface
        self.reset_()


    def reset_(self):
        """replace toutes briques selon leur situation initiale"""
        self.bricks = self.liste_briques()

    def dessine_moi(self):
        """affiche les textures de toutes briques à leurs coordonnées"""
        for ligne in self.bricks:
            for brique in ligne:
                brique.affiche()


    def liste_briques(self):
        """création de liste des coordonnées des briques pour l'affichage"""
        x_base, y_base = 45, 82
        x_repet, y_repet = 12, 11
        briques = [[] for _ in range(y_repet)]
        for y in range(y_repet):
            for x in range(x_repet): briques[y].append(brick(x_base + x * 90, y_base + y * 28, self.img["blue"], self.surface, 1))
        return briques

    def __str__(self):
        """affiche la liste des briques dans la console"""
        str_ = ""
        for ligne in self.bricks:
            for brique in ligne:
                str_ += f"{brique.x, brique.y} "
            str_ += "\n"
        return str_

## Class Brick
"""définition d'une brique avec sa texture, ces variations et sa position"""

class brick:
    def __init__(self, x, y, img, surface, hp = 1):
        self.taille_x = 43
        self.taille_y = 12
        self.x = x
        self.y = y
        self.x_min = self.x - self.taille_x
        self.x_max = self.x + self.taille_x
        self.y_min = self.y - self.taille_y
        self.y_max = self.y + self.taille_y
        self.hp = self.max_hp = hp
        self.en_vie = True
        self.coul = (0, 255, 0)
        self.img = img
        self.surface = surface
        self.layer_cassure = None

    def ch_coul(self):
        '''jsp'''
        self.coul = (0, 0, 255)

    def hp_add(self, nb):
        '''actualise le nombre de points de vie que possède la brique et retourne False si elle n'a plus de vie'''
        if self.en_vie: self.hp += nb
        if self.hp < 1: self.en_vie = False

    def kill(self):
        '''tue la brique'''
        self.en_vie = False

    def cassure(self, liste_fissure):
        if self.en_vie :
            if (self.max_hp//3)*2 < self.hp <= self.max_hp :
                self.layer_cassure = liste_fissure["fissure1"]
            elif self.max_hp//3 < self.hp <= (self.max_hp//3)*2 :
                self.layer_cassure = liste_fissure["fissure2"]
            elif 0 < self.hp <= self.max_hp//3 :
                self.layer_cassure = liste_fissure["fissure3"]

    def affiche(self):
        if self.en_vie:
            self.surface.blit(self.img, (self.x - self.taille_x, self.y - self.taille_y))
            if not self.layer_cassure is None:
                self.surface.blit(self.layer_cassure, (self.x - self.taille_x, self.y - self.taille_y))
