import Arma
import pygame

class PuñosFuera(Arma.Arma):
    def __init__(self):
        self.__puñosOn=pygame.image.load('./PuñosOn.png')

    def enciende(self,screen):
        screen.blit(self.__puñosOn,(0,0))
        pygame.display.flip()

    def grito(self):
        print('¡¡¡¡Puños, fuera!!!!')