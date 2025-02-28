import pygame
from skill import Skill

pygame.init()

class Player():
    def __init__(self, x, y, left, right, skill, screen):
        self.x = x
        self.y = y
        self.left = left
        self.right = right
        self.isJump = False
        self.jumpHeight = 12
        self.speed = 5
        self.isAlive = True
        self.walk_images_r = [
            pygame.image.load('image/walk0.png'),
            pygame.image.load('image/walk1.png')
        ]
        self.walk_images_l = [
            pygame.transform.flip(self.walk_images_r[0], True, False),
            pygame.transform.flip(self.walk_images_r[1], True, False)
        ]
        self.animation_index = 0  # Track animation frame
        self.animation_delay = 10  # Frames to wait before switching
        self.animation_counter = 0
        self.PlayerImage = self.walk_images_l[0]  # Start with left image
        self.player = self.PlayerImage.get_rect()
        self.player.center = (x, y)
        self.skill = skill
        self.TimeCast = 0
        self.playerLoc = [x, y]
        self.screen = screen
        self.cast = Skill(self.playerLoc, self.screen)

        if skill == 'shield':
            self.SkillCooldown = 15
        elif skill == 'meteor':
            self.SkillCooldown = 20
        elif skill == 'blind':
            self.SkillCooldown = 25

    def draw(self, screen):
        self.player.center = (self.x, self.y)
        screen.blit(self.PlayerImage, self.player)

    def move(self, key, screen):
        if not self.isAlive:
            return

        w, h = screen.get_size()
        moving = False  # Track movement

        if key[self.left] and self.x > 15:
            self.x -= self.speed
            self.PlayerImage = self.walk_images_l[self.animation_index]
            moving = True

        if key[self.right] and self.x < w - 15:
            self.x += self.speed
            self.PlayerImage = self.walk_images_r[self.animation_index]
            moving = True

        # Animation logic
        if moving:
            self.animation_counter += 1
            if self.animation_counter >= self.animation_delay:
                self.animation_index = (self.animation_index + 1) % 2  # Toggle between 0 and 1
                self.animation_counter = 0
        else:
            self.animation_index = 0  # Reset when standing still

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

    def isHit(self, enemy):
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
        self.playerLoc = (self.x, self.y)
        self.cast = Skill(self.playerLoc, self.screen)

    def skillCast(self):
        if self.skill == 'meteor':
            self.cast.meteor()
        elif self.skill == 'blind':
            self.cast.blind()

    def meteorLoc(self):
        return self.cast.getAttackLoc()
