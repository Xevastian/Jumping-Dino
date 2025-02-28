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
        self.image1r = pygame.image.load('image/LEN1.png')
        self.image1l = pygame.transform.flip(self.image1r, True, False)
        self.image2r = pygame.image.load('image/LEN2.png')
        self.image2l = pygame.transform.flip(self.image2r, True, False)
        self.image3r = pygame.image.load('image/LEN3.png')
        self.image3l = pygame.transform.flip(self.image3r, True, False)
        self.image4r = pygame.image.load('image/LEN4.png')
        self.image4l = pygame.transform.flip(self.image4r, True, False)
        if count == 0:
            self.boxImg = self.image1l
        elif self.dir == 0:
            if self.count == 1:
                self.boxImg = self.image1r 
            elif self.count == 2:
                self.boxImg = self.image2r 
            elif self.count == 3:
                self.boxImg = self.image3r 
            elif self.count == 4:
                self.boxImg = self.image4r
        else:
            if self.count == 1:
                self.boxImg = self.image1l 
            elif self.count == 2:
                self.boxImg = self.image2l 
            elif self.count == 3:
                self.boxImg = self.image3l 
            elif self.count == 4:
                self.boxImg = self.image4l
        self.box = self.boxImg.get_rect()
        self.box.center = (self.x,self.y)
    
    def draw(self,screen):
        if self.dir == 1:
            if self.x < -160:
                self.count = random.randint(self.level[0],self.level[1])
                self.s = random.randint(self.speed[0],self.speed[1])
                self.dir = random.randint(0,1)
                self.height = random.randint(0,1)
                self.x = 1280 if self.dir == 1 else -160
                self.y = (self.y_axis - 10) if self.height == 1 else self.y_axis + 40
        else:
            if self.x > 1280 :
                self.count = random.randint(self.level[0],self.level[1])
                self.s = random.randint(self.speed[0],self.speed[1])
                self.dir = random.randint(0,1)
                self.height = random.randint(0,1)
                self.x = 1280 if self.dir == 1 else -160
                self.y = (self.y_axis - 10) if self.height == 1 else self.y_axis + 40
            if self.dir == 0:
                if self.count == 1:
                    self.boxImg = self.image1r 
                elif self.count == 2:
                    self.boxImg = self.image2r 
                elif self.count == 3:
                    self.boxImg = self.image3r 
                elif self.count == 4:
                    self.boxImg = self.image4r
            else:
                if self.count == 1:
                    self.boxImg = self.image1l 
                elif self.count == 2:
                    self.boxImg = self.image2l 
                elif self.count == 3:
                    self.boxImg = self.image3l 
                elif self.count == 4:
                    self.boxImg = self.image4l
        self.box.center = (self.x,self.y)
        self.x = self.x - self.s if self.dir == 1 else self.x + self.s
        if self.count == 0:
            print("invis")
            return
        screen.blit(self.boxImg,self.box)