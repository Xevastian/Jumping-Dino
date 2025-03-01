import pygame
import random
pygame.init()

class Meteor():
    def __init__(self, location):
        self.speed = 1
        self.size = 40
        self.location = location
        self.x = location[0] 
        self.y = 0 if self.location[1] > 360 else 361
        self.box = pygame.Rect(self.x,self.y,40,40)

    def draw(self,screen):
        self.speed += 0.006
        self.size += 1.5
        self.y += self.speed
        self.box.update(self.x - (self.size / 2),self.y,self.size, self.size)
        pygame.draw.rect(screen,'Black',self.box)
        pygame.draw.rect(screen, (255, 0, 0), self.box, 2)

    def AttackLoc(self):
        return self.box