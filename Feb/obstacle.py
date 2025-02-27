import pygame
import random
pygame.init()

class Obstacle():
    def __init__(self,count, y_axis,level,speed):
        self.count = count
        self.level = level
        self.s =random.randint(speed[0],speed[1])
        self.speed = speed
        self.dir = random.randint(0,1)
        self.height = random.randint(0,1)
        self.x = 1280 if self.dir == 1 else -160
        self.y = y_axis - 10 if self.height == 1 else y_axis + 40
        self.y_axis = y_axis
        self.box = pygame.Rect(self.x,self.y,40*self.count,40)

    
    def draw(self,screen):
        if self.dir == 1:
            if self.x < -160:
                self.count = random.randint(self.level[0],self.level[1])
                print(f'Count: { self.count}')
                self.s = random.randint(self.speed[0],self.speed[1])
                self.dir = random.randint(0,1)
                self.height = random.randint(0,1)
                self.x = 1280 if self.dir == 1 else -160
                self.y = (self.y_axis - 10) if self.height == 1 else self.y_axis + 40
        else:
            if self.x > 1280 :
                self.count = random.randint(self.level[0],self.level[1])
                print(f'Count: { self.count}')
                self.s = random.randint(self.speed[0],self.speed[1])
                self.dir = random.randint(0,1)
                self.height = random.randint(0,1)
                self.x = 1280 if self.dir == 1 else -160
                self.y = (self.y_axis - 10) if self.height == 1 else self.y_axis + 40
        self.box.update(self.x,self.y,self.count*40,40)
        self.x = self.x - self.s if self.dir == 1 else self.x + self.s
        pygame.draw.rect(screen,'Black',self.box)