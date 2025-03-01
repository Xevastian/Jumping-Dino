import pygame
import random
import time
from player import Player
from utilSkill import load_save_skill
from obstacle import Obstacle
from util import load_save
from button import Button

pygame.init()  

class Game:
    def __init__(self,screen,skill1,skill2):
        self.skillSave = load_save_skill()['skill']
        self.save = load_save()
        self.start_time = time.monotonic()        
        self.clock = pygame.time.Clock()          
        self.bgImage = pygame.image.load('image/bg.png')
        self.x, self.y = 1280,720                       # Window size
        self.screen = screen
        self.groundImage = pygame.image.load('image/ground.png')
        self.ground1 = self.groundImage.get_rect()
        self.ground2 = self.groundImage.get_rect()
        self.ground1.center = (640,670)
        self.ground2.center = (640,310)

        # Setting Charaaacters and variables
        level = [0,3]
        speed = [5,7]
        self.player1 = Player(640,600,self.save['controls']['player1']['Left'],self.save['controls']['player1']['Right'],self.skillSave['player1'],self.screen)
        self.obs1 = Obstacle(random.randint(level[0],level[1]),540,level,speed)
        self.obs2 = Obstacle(random.randint(level[0],level[1]),540,level,speed)

        self.player2 = Player(640,240,self.save['controls']['player2']['Left'],self.save['controls']['player2']['Right'],self.skillSave['player2'],self.screen) 
        self.obs3 = Obstacle(random.randint(level[0],level[1]),180, level,speed)
        self.obs4 = Obstacle(random.randint(level[0],level[1]),180, level,speed)

        # Fora game over and scoring
        self.font = pygame.font.Font('FreeSansBold.ttf', 32) # setting font
        self.text = self.font.render('Game Over', True, "Black")
        self.textRect1 = self.text.get_rect()
        self.textRect1.center = (640,450)
        self.textRect2 = self.text.get_rect()
        self.textRect2.center = (640,90)

    def start(self):
        # countdown
       
        p1SkillImage = pygame.image.load('image/' + self.player1.skill + '.png')
        p2SkillImage = pygame.image.load('image/' + self.player2.skill + '.png')
        stage = 1
        p1CD = p1SkillImage.get_rect()
        p2CD = p2SkillImage.get_rect()
        p1CD.center, p2CD.center = (70,430), (70,70)
        for i  in range(3,-1,-1):
            cd = self.font.render(str(i),True,"Black")
            cdRect = cd.get_rect()
            cdRect.center = (640,360)
            self.screen.blit(self.bgImage, (0, 0)) 
            self.player1.draw(self.screen) 
            self.player2.draw(self.screen) 
            self.screen.blit(self.groundImage,self.ground1)
            self.screen.blit(self.groundImage,self.ground2)
            self.screen.blit(cd,cdRect)
            pygame.display.update()
            self.clock.tick(60)
            time.sleep(1)


        count = p1Score = p2Score = 0
        running = True
        ticks = 60
        p1Key = self.save['controls']['player1']['Skill']
        p2Key = self.save['controls']['player2']['Skill']
        while (self.player1.isAlive or self.player2.isAlive) and running:
            count += 1
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    pygame.key.name(event.key)
                    if event.key == self.save['controls']['player1']['Jump']:
                        self.player1.isJump = True
                    if event.key == self.save['controls']['player2']['Jump']:
                        self.player2.isJump = True
                    if(event.key == p1Key and self.player1.SkillCooldown < 1 and self.player1.isAlive):
                        self.player1.skillTrigger()
                        print('hey')
                    if(event.key == p2Key and self.player2.SkillCooldown < 1 and self.player2.isAlive): # meaning activate
                        self.player2.skillTrigger()
                        print('hey')
            # Movements
            self.player1.move(key,self.screen)
            self.player1.jump()
            self.player2.move(key,self.screen)
            self.player2.jump()
            # Display
            score1 = self.font.render(str(p1Score),True,"Black")
            scoreRect1 = score1.get_rect()
            scoreRect1.center = (1200,410)
            score2 = self.font.render(str(p2Score),True,"Black")
            scoreRect2 = score2.get_rect()
            scoreRect2.center = (1200,50)
            self.screen.blit(self.bgImage, (0, 0)) 
            self.screen.blit(score1,scoreRect1)
            self.screen.blit(score2,scoreRect2)
        
            # Computations and variable display
            if (self.player1.isHit(self.obs1.box) and self.obs1.count != 0) or (self.player1.isHit(self.obs2.box) and self.obs2.count != 0) or (self.player1.isHit(self.player2.meteorLoc()) and self.player2.TimeCast > 0):
                if(self.player1.skill == 'shield' and self.player1.TimeCast > 0):
                    self.player1.isAlive = True
                else:
                    if self.player1.isAlive:
                        time.sleep(3)
                    self.player1.isAlive = False
                    
            if self.player1.isAlive:
                self.player1.move(key,self.screen)
                self.player1.jump()
                self.obs1.draw(self.screen)
                self.obs2.draw(self.screen)
                p1SkillCD = self.font.render(str(self.player1.SkillCooldown) if self.player1.SkillCooldown > 0 else '',True,"Black")
                p1SkillCDRect = p1SkillCD.get_rect()
                p1SkillCDRect.center = (70,430)
                self.screen.blit(p1SkillImage,p1CD)
                self.screen.blit(p1SkillCD,p1SkillCDRect)
                if(count % 60 == 0):
                    p1Score += 1
            else:
                self.screen.blit(self.text, self.textRect1) 
            
            if (self.player2.isHit(self.obs3.box) and self.obs3.count != 0) or (self.player2.isHit(self.obs4.box) and self.obs4.count != 0) or (self.player2.isHit(self.player1.meteorLoc()) and self.player1.TimeCast > 0):
                if(self.player2.skill == 'shield' and self.player2.TimeCast > 0):
                    self.player2.isAlive = True
                else:
                    if self.player2.isAlive:
                        time.sleep(3)
                    self.player2.isAlive = False
                    
            if self.player2.isAlive:
                self.player2.move(key,self.screen)
                self.player2.jump()
                self.obs3.draw(self.screen)
                self.obs4.draw(self.screen)
                p2SkillCD = self.font.render(str(self.player2.SkillCooldown) if self.player2.SkillCooldown > 0 else '',True,"Black")
                p2SkillCDRect = p2SkillCD.get_rect()
                p2SkillCDRect.center = (70,70)
                self.screen.blit(p2SkillImage,p2CD)   
                self.screen.blit(p2SkillCD,p2SkillCDRect)           
                if(count % 60 == 0):
                    p2Score += 1
            else:
                self.screen.blit(self.text, self.textRect2) 

            # Will cool the skill and cast
            if count % 60 == 0:  
                if self.player1.SkillCooldown > 0:
                    self.player1.SkillCooldown -= 1
                if self.player2.SkillCooldown > 0:
                    self.player2.SkillCooldown -= 1
                if self.player1.TimeCast > 0:
                    self.player1.TimeCast -= 1
                if self.player2.TimeCast > 0:
                    self.player2.TimeCast -= 1
                
            if count % (60 * 25) == 0:
                if stage == 7:
                    continue
                ticks += 10
                stage += 1
                if stage == 2:
                    self.obs1.level = [1,3]
                    self.obs2.level = [1,3]
                    self.obs3.level = [1,3]
                    self.obs4.level = [1,3]
                elif stage == 3:
                    self.obs1.level = [2,3]
                    self.obs2.level = [2,3]
                    self.obs3.level = [2,3]
                    self.obs4.level = [2,3]
                elif stage == 3:
                    self.obs1.level = [3,3]
                    self.obs2.level = [3,3]
                    self.obs3.level = [3,3]
                    self.obs4.level = [3,3]
                elif stage == 4:
                    self.obs1.level = [3,4]
                    self.obs2.level = [3,4]
                    self.obs3.level = [3,4]
                    self.obs4.level = [3,4]
                elif stage == 5:
                    self.obs1.speed = [6,7]
                    self.obs2.speed = [6,7]
                    self.obs3.speed = [6,7]
                    self.obs4.speed = [6,7]
                elif stage == 6:
                    self.obs1.speed = [6,8]
                    self.obs2.speed = [6,8]
                    self.obs3.speed = [6,8]
                    self.obs4.speed = [6,8]                    
                print(f'Stage: {stage}')
            
            self.player1.draw(self.screen) 
            self.player2.draw(self.screen) 
  
            if self.player2.TimeCast > 0:
                self.player2.skillCast()        

            if self.player1.TimeCast > 0: 
                self.player1.skillCast()
            
            self.screen.blit(self.groundImage,self.ground1)
            self.screen.blit(self.groundImage,self.ground2)
            pygame.display.update()
            self.clock.tick(ticks)
            

        # countdown
        for i  in range(5,-1,-1):
            cd = self.font.render(str(i),True,"Black")
            congrats = self.font.render('Winner!',True,"Black")
            cdRect,congratsRect = cd.get_rect() , congrats.get_rect()
            cdRect.center = (1200,50)
            congratsRect.center = (640,180) if p1Score < p2Score else (640,540)
            self.screen.blit(self.bgImage, (0, 0)) 

            self.player1.draw(self.screen) 
            self.player2.draw(self.screen) 
            self.screen.blit(self.groundImage,self.ground1)
            self.screen.blit(self.groundImage,self.ground2)
            self.screen.blit(cd,cdRect)
            self.screen.blit(congrats,congratsRect)
            pygame.display.update()
            self.clock.tick(60)
            time.sleep(1)

        return     