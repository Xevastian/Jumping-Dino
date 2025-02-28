import pygame
import random
pygame.init()

class Obstacle():
    def __init__(self, count, y_axis, level, speed):
        self.count = count
        self.level = level
        self.s = random.randint(speed[0], speed[1])
        self.speed = speed
        self.dir = random.randint(0, 1)  # 0: Right, 1: Left
        self.height = random.randint(0, 1)
        self.x = 1280 if self.dir == 1 else -160
        self.y = y_axis - 10 if self.height == 1 else y_axis + 40
        self.y_axis = y_axis

        # Load images
        self.image1r = pygame.image.load('image/LEN1.png')
        self.image1l = pygame.transform.flip(self.image1r, True, False)
        self.image2r = pygame.image.load('image/LEN2.png')
        self.image2l = pygame.transform.flip(self.image2r, True, False)
        self.image3r = pygame.image.load('image/LEN3.png')
        self.image3l = pygame.transform.flip(self.image3r, True, False)
        self.image4r = pygame.image.load('image/LEN4.png')
        self.image4l = pygame.transform.flip(self.image4r, True, False)
        
        self.update_image()
        
        self.box = self.boxImg.get_rect()
        self.box.center = (self.x, self.y)
    
    def update_image(self):
        if self.dir == 1:  # Moving left
            self.boxImg = [self.image1l, self.image2l, self.image3l, self.image4l][self.count - 1]
        else:  # Moving right
            self.boxImg = [self.image1r, self.image2r, self.image3r, self.image4r][self.count - 1]

    def draw(self, screen):
        if self.dir == 1 and self.x < -160 or self.dir == 0 and self.x > 1280:
            self.count = random.randint(self.level[0], self.level[1])
            self.s = random.randint(self.speed[0], self.speed[1])
            self.dir = random.randint(0, 1)
            self.height = random.randint(0, 1)
            self.x = 1280 if self.dir == 1 else -160
            self.y = self.y_axis - 10 if self.height == 1 else self.y_axis + 40
            self.update_image()

        self.box.center = (self.x, self.y)
        self.x = self.x - self.s if self.dir == 1 else self.x + self.s
        if self.count == 0:
            return
        screen.blit(self.boxImg, self.box)
