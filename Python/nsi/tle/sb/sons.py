import pygame
pygame.init()
pygame.mixer.init()

class son_jeu:

    def __init__(self):
        self.playlist = set()


    def joue(self):
        if self.playlist != set():
            for i in self.playlist:
                pygame.mixer.music.load(i)
            pygame.mixer.music.play(0)
            self.playlist.clear()


    def son_perdu(self):
        self.playlist.add(r"sounds\player_lose.mp3")


    def son_collbords(self):
        self.playlist.add(r"sounds\wall_collision.mp3")


    def son_briques1(self):
        self.playlist.add(r"sounds\brick_collision.mp3")



    def son_briques2(self):
        self.playlist.add(r"sounds\brick_breaker.mp3")


    def son_balle_barre(self):
        self.playlist.add(r"sounds\stick_collision.mp3")