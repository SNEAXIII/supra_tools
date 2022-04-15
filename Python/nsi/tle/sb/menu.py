import pygame
from niveaux import liste_level_0, liste_level_1, liste_level_2, liste_level_3, liste_level_4


class souris:
    def __init__(self):
        self.press = False
        self.position()

    def position(self):
        self.pos = pygame.mouse.get_pos()


## Class Menu
''' Création du Menu du jeu qui s'occupera de lancer les différentes configurations de fenêtres pour le jeu, les options, les crédits et les niveaux '''


class Menu:

    def __init__(self, surface, font, souris):
        self.souris = souris
        self.surface = surface
        self.jouer = Bouton(surface, 350, 261, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png",
                            "JOUER", font, self.souris)
        self.levels = Bouton(surface, 350, 413, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png",
                             "NIVEAUX", font, self.souris)
        self.credits = Bouton(surface, 20, 585, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png",
                              "CREDITS", font, self.souris)
        self.quitter = Bouton(surface, 675, 585, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png",
                              "QUITTER", font, self.souris)
        self.font = font
        self.reset()

    def verif_bouton(self):
        self.jouer.verif()
        self.credits.verif()
        self.levels.verif()
        self.quitter.verif()

    def change_texture_bouton(self):
        self.jouer.change_textu()
        self.credits.change_textu()
        self.levels.change_textu()
        self.quitter.change_textu()

    def affiche_bouton(self):
        self.jouer.afficher()
        self.credits.afficher()
        self.levels.afficher()
        self.quitter.afficher()

    def affiche_texte(self):
        self.jouer.affiche_texte()
        self.levels.affiche_texte()
        self.credits.affiche_texte()
        self.quitter.affiche_texte()

    def click(self):
        if self.jouer.click():
            # Affiche le jeu avec les paramètres sélectionnés
            self.jeu = True
        elif self.credits.click():
            # Afficher l'image des crédits
            pass
        elif self.levels.click():
            # Afficher les boutons des niveaux
            self.level = True
        elif self.quitter.click():
            # Quitte la fenêtre Pygame et clos le programme
            self.end = True

    def reset(self):
        self.end = False
        self.jeu = False
        self.level = False


## Class Bouton
'''Création des boutons du Menu du jeu'''


class Bouton:

    def __init__(self, surface, x, y, taille_x, taille_y, image_simple, image_souris, texte, font, souris):
        self.surface = surface
        self.x = x
        self.y = y
        self.taille_x = taille_x
        self.taille_y = taille_y
        self.image_simple = self.image_actuelle = pygame.image.load(image_simple)
        self.image_souris = pygame.image.load(image_souris)
        self.str = texte
        self.text = font.render(texte, True, (0, 0, 0))
        self.souris_dedans = False
        self.souris = souris

    def __str__(self):
        '''affiche rien'''
        return f"{self.text} -> {self.x} , {self.y}"

    def afficher(self):
        '''affiche la texture du bouton'''
        self.surface.blit(self.image_actuelle, (self.x, self.y))

    def verif(self):
        '''vérifie si le curseur de la souris et dans l'aire du bouton'''
        if self.x <= self.souris.pos[0] <= self.x + self.taille_x and self.y <= self.souris.pos[
            1] <= self.y + self.taille_y:
            self.souris_dedans = True
        else:
            self.souris_dedans = False

    def change_textu(self):
        '''change la texture à afficher en fonction de verif'''
        if self.souris_dedans:
            self.image_actuelle = self.image_souris
        else:
            self.image_actuelle = self.image_simple

    def click(self):
        if self.souris.press and self.souris_dedans:
            return True

    def affiche_texte(self):
        self.surface.blit(self.text, (
        self.x + (self.taille_x / 2) - (len(self.str) / 2) * 30 - 15, self.y + self.taille_y / 2 - 30))


# suggestion pour l'affichage de la fenêtre des niveaux
# toutes les idées en bazar, bonne lecture xD
## Class Level
''' Création de l'orga de la fenêtre niveaux'''
'''
(surface, x, y, taille_x, taille_y, textu_petite, textu_grande, texte_afficher, font, pattern de briques ( lst ), vitesse_ball, change_barre)
level_1 = Level(surface, 90, 45, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png", "niveau 1", font, lst_lvl_1, 6, Barre.augmente_taile_x(-1)) # level_1.png
level_2 = Level(surface, 565, 45, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png", "niveau 2", font, lst_lvl_2, 8, Barre.augmente_taile_x(0)) # level_2.png
level_3 = Level(surface, 90, 215, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png", "niveau 3", font, lst_lvl_3, z,  Barre.augmente_taile_x(-2)) # level_3.png
level_3 = Level(surface, 565, 215, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png", "niveau 4", font, lst_lvl_4, z,  Barre.augmente_taile_x(-3)) # level_4.png
'''


class Menu_Level:

    def __init__(self, surface, font, souris):
        self.souris = souris
        self.surface = surface
        self.retour = Bouton(surface, 347, 538, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png", "RETOUR", font, souris)
        self.bouton_level_1 = Bouton(surface, 109, 109, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png", "niveau 1", font, souris)
        self.bouton_level_2 = Bouton(surface, 595, 109, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png", "niveau 2", font, souris)
        self.bouton_level_3 = Bouton(surface, 109, 323, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png", "niveau 3", font, souris)
        self.bouton_level_4 = Bouton(surface, 595, 323, 385, 115, "bouton_jouer_clear.png", "bouton_jouer_souris.png", "niveau 4", font, souris)
        self.level_1 = Niveau(liste_level_1, 6, -2, 55, 2, 3)
        self.level_2 = Niveau(liste_level_2, 7, -5, 25, 3, 2)
        self.level_3 = Niveau(liste_level_3, 8, -6, 45, 3, 2)
        self.level_4 = Niveau(liste_level_4, 10, -8, 20, 3, 1)
        self.reset()
        self.font = font

    def verif_bouton(self):
        self.bouton_level_1.verif()
        self.bouton_level_2.verif()
        self.bouton_level_3.verif()
        self.bouton_level_4.verif()
        self.retour.        verif()

    def change_texture_bouton(self):
        self.bouton_level_1.change_textu()
        self.bouton_level_2.change_textu()
        self.bouton_level_3.change_textu()
        self.bouton_level_4.change_textu()
        self.retour.        change_textu()

    def affiche_bouton(self):
        self.bouton_level_1.afficher()
        self.bouton_level_2.afficher()
        self.bouton_level_3.afficher()
        self.bouton_level_4.afficher()
        self.retour.        afficher()

    def affiche_texte(self):
        self.bouton_level_1.affiche_texte()
        self.bouton_level_2.affiche_texte()
        self.bouton_level_3.affiche_texte()
        self.bouton_level_4.affiche_texte()
        self.retour.        affiche_texte()

    def click(self):
        if self.bouton_level_1.click():
            # Lance le jeu avec les paramètres choisis
            return self.level_1

        elif self.bouton_level_2.click():
            # Lance le jeu avec les paramètres choisis
            return self.level_2

        elif self.bouton_level_3.click():
            # Lance le jeu avec les paramètres choisis
            return self.level_3

        elif self.bouton_level_4.click():
            # Lance le jeu avec les paramètres choisis
            return self.level_4

        elif self.retour.click():
            # Retourne sur le menu de base
            self.end = True
            return False

        else:
            return False

    def reset(self):
        self.end = False


class Niveau:

    def __init__(self, pattern, vitesse_ball, change_barre, angle_depart, hp_brique, hp):
        self.pattern = pattern
        self.vitesse = vitesse_ball
        self.taille_barre = change_barre
        self.angle = angle_depart
        self.hp_brique = hp_brique
        self.hp_ball = hp
