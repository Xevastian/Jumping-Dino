import pygame
from meteor import Meteor
pygame.init()

class Skill:
    def __init__(self,location,screen):
        self.location = location
        self.screen = screen
        self.meteorAttack = Meteor(location)
        

    def blind(self):
        y = 0 if self.location[1] > 360 else 360
        box = pygame.Rect(self.location[0] - 300, y, 600, 260)
        pygame.draw.rect(self.screen,"Black",box)
            
    def meteor(self):
        self.meteorAttack.draw(self.screen)
    
    def getAttackLoc(self):
        return self.meteorAttack.AttackLoc()