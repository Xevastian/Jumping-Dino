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
        self.image = pygame.image.load('image/attack.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.box = pygame.Rect(self.x, self.y, 40, 40)

    def draw(self,screen):
        self.speed += 0.006
        self.size += 1.5
        self.y += self.speed
        scaled_image = pygame.transform.scale(self.image, (int(self.size), int(self.size)))
        new_x = self.x - (self.size / 2)
        new_y = self.y
        self.box.update(new_x, new_y, self.size, self.size)
        screen.blit(scaled_image, (new_x, new_y))
        #pygame.draw.rect(screen, (255, 0, 0), self.box, 2)

    def AttackLoc(self):
        return self.box