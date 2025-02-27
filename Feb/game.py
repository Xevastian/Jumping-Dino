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
        self.start_time = time.monotonic()        # For counting scores
        self.clock = pygame.time.Clock()          # For game ticks #60 frames every second

        self.x, self.y = 1280,720                       # Window size
        self.screen = screen
        self.ground1 = pygame.Surface((1280, 100))
        self.ground2 = pygame.Surface((1280, 100)) # setting grounds
        self.ground1.fill('Green')
        self.ground2.fill('Green')

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
        stage = 1
        p1CD = Button(70,430,70,70,self.player1.SkillCooldown)
        p2CD = Button(70,70,70,70,self.player2.SkillCooldown)
        for i  in range(3,-1,-1):
            cd = self.font.render(str(i),True,"Black")
            cdRect = cd.get_rect()
            cdRect.center = (640,360)
            self.screen.fill("White")
            self.player1.draw(self.screen) 
            self.player2.draw(self.screen) 
            self.screen.blit(self.ground1,(0,620))
            self.screen.blit(self.ground2,(0,260))
            self.screen.blit(cd,cdRect)
            pygame.display.update()
            self.clock.tick(60)
            time.sleep(1)


        count = p1Score = p2Score = 0
        running = True
        ticks = 60
        while (self.player1.isAlive or self.player2.isAlive) and running:
            count += 1
            # Events // key pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    pygame.key.name(event.key)
                    if event.key == self.save['controls']['player1']['Jump']:
                        self.player1.isJump = True
                    if event.key == self.save['controls']['player2']['Jump']:
                        self.player2.isJump = True
            
            # Detecting key hold
            key = pygame.key.get_pressed()

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
            self.screen.fill('White')
            self.screen.blit(score1,scoreRect1)
            self.screen.blit(score2,scoreRect2)
        
            # Computations and variable display
            if self.player1.isHit(self.obs1.box) or self.player1.isHit(self.obs2.box) or (self.player1.isHit(self.player2.meteorLoc()) and self.player2.TimeCast > 0):
                if(self.player1.skill == 'shield' and self.player1.TimeCast > 0):
                    self.player1.isAlive = True
                else:
                    self.player1.isAlive = False
            if self.player1.isAlive:
                self.player1.move(key,self.screen)
                self.player1.jump()
                self.obs1.draw(self.screen)
                self.obs2.draw(self.screen)
                p1CD.text = str(self.player1.SkillCooldown) if self.player1.SkillCooldown > 0 else ''
                p1CD.draw(self.screen)
                if(count % 60 == 0):
                    p1Score += 1
            else:
                self.screen.blit(self.text, self.textRect1) 
            
            if self.player2.isHit(self.obs3.box) or self.player2.isHit(self.obs4.box) or (self.player2.isHit(self.player1.meteorLoc()) and self.player1.TimeCast > 0):
                if(self.player2.skill == 'shield' and self.player2.TimeCast > 0):
                    self.player2.isAlive = True
                else:
                    self.player2.isAlive = False
            if self.player2.isAlive:
                self.player2.move(key,self.screen)
                self.player2.jump()
                self.obs3.draw(self.screen)
                self.obs4.draw(self.screen)
                p2CD.text = str(self.player2.SkillCooldown) if self.player2.SkillCooldown > 0 else ''
                p2CD.draw(self.screen)
                if(count % 60 == 0):
                    p2Score += 1
            else:
                self.screen.blit(self.text, self.textRect2) 
            
            self.player1.draw(self.screen) 
            self.player2.draw(self.screen) 

            if(key[self.save['controls']['player2']['Skill']] == True and self.player2.SkillCooldown <= 0 and self.player2.isAlive): # meaning activate
                self.player2.skillTrigger()
            if self.player2.TimeCast > 0: # will draw the skill
                self.player2.skillCast()
            
            # Will cool the skill and cast
            if self.player2.SkillCooldown > 0 and count % 60 == 0:
                self.player2.SkillCooldown -= 1

            if self.player2.TimeCast > 0 and count % 60 == 0:
                self.player2.TimeCast -= 1

            if(key[self.save['controls']['player1']['Skill']] == True and self.player1.SkillCooldown <= 0 and self.player1.isAlive): # meaning activate
                self.player1.skillTrigger()
            if self.player1.TimeCast > 0: # will draw the skill
                self.player1.skillCast()

            if self.player1.SkillCooldown > 0 and count % 60 == 0:
                self.player1.SkillCooldown -= 1

            if self.player1.TimeCast > 0 and count % 60 == 0:
                self.player1.TimeCast -= 1
            self.screen.blit(self.ground1,(0,620))
            self.screen.blit(self.ground2,(0,260))
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
            pygame.display.update()
            self.clock.tick(ticks)
            

        # countdown
        for i  in range(5,-1,-1):
            cd = self.font.render(str(i),True,"Black")
            congrats = self.font.render('Winner!',True,"Black")
            cdRect,congratsRect = cd.get_rect() , congrats.get_rect()
            cdRect.center = (1200,50)
            congratsRect.center = (640,180) if p1Score < p2Score else (640,540)
            self.screen.fill("White")

            self.player1.draw(self.screen) 
            self.player2.draw(self.screen) 
            self.screen.blit(self.ground1,(0,620))
            self.screen.blit(self.ground2,(0,260))
            self.screen.blit(cd,cdRect)
            self.screen.blit(congrats,congratsRect)
            pygame.display.update()
            self.clock.tick(60)
            time.sleep(1)

        return     