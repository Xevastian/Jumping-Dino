import pygame
from skill import Skill
pygame.init()

class Player():
    def __init__(self,x,y,left,right,skill,screen):
        self.x = x
        self.y = y
        self.left = left
        self.right = right
        self.isJump = False
        self.jumpHeight = 12
        self.speed = 5
        self.isAlive = True
        self.player = pygame.Rect(x,y,40,40)
        self.skill = skill
        self.TimeCast = 0
        self.playerLoc = [x,y]
        self.screen = screen
        self.cast = Skill(self.playerLoc,self.screen)
        if skill == 'shield':
            self.SkillCooldown = 15
        elif skill == 'meteor':
            self.SkillCooldown = 20
        elif skill == 'blind':
            self.SkillCooldown = 25
        



    def draw(self,screen):
        self.player.center = (self.x,self.y)
        pygame.draw.rect(screen,"Red",self.player)

    def move(self,key,screen):
        if not self.isAlive:
            return
        w,h = screen.get_size()
        if key[self.left] and self.x > 15:
            self.x -= self.speed
        if key[self.right] and self.x < w - 15:
            self.x += self.speed

    def jump(self):
        if not self.isAlive:
            return
        if self.isJump:
                if self.jumpHeight >= -12:
                    neg = 1
                    if self.jumpHeight < 0:
                        neg = -1
                    self.y -= self.jumpHeight**2 * 0.1 * neg
                    self.jumpHeight -= 0.5
                else:
                    self.isJump = False
                    self.jumpHeight = 12

    def isHit(self,enemy):
        return self.player.colliderect(enemy)
    
    def skillTrigger(self):
        if self.skill == 'shield':
            self.SkillCooldown = 15
            self.TimeCast = 2
        elif self.skill == 'meteor':
            self.SkillCooldown = 20
            self.TimeCast = 2
        elif self.skill == 'blind':
            self.SkillCooldown = 23
            self.TimeCast = 5
        self.playerLoc = (self.x,self.y)
        self.cast = Skill(self.playerLoc,self.screen)
        
    def skillCast(self):
        if self.skill == 'meteor':
            self.cast.meteor()
        elif self.skill == 'blind':
            self.cast.blind()
    
    def meteorLoc(self):
        return self.cast.getAttackLoc()