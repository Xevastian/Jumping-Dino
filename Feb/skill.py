import pygame
from meteor import Meteor
pygame.init()

class Skill:
    def __init__(self,location,screen):
        self.location = location
        self.screen = screen
        self.meteorAttack = Meteor(location)
        self.blind_image = pygame.image.load('image/attack2.png')
        self.blind_image = pygame.transform.scale(self.blind_image, (600, 260))

    def blind(self):
        y = 0 if self.location[1] > 360 else 360
        self.screen.blit(self.blind_image, (self.location[0] - 300, y))
            
    def meteor(self):
        self.meteorAttack.draw(self.screen)
    
    def getAttackLoc(self):
        return self.meteorAttack.AttackLoc()