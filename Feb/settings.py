import pygame
from button import Button

pygame.init()

class Settings:
    def __init__(self, screen,p1KL,p1KR,p1KJ,p1KS,p2KL,p2KR,p2KJ,p2KS,sfmv,sfxv):
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.p1KL, self.p1KR, self.p1KJ, self.p1KS = p1KL, p1KR, p1KJ, p1KS
        self.p2KL, self.p2KR, self.p2KJ, self.p2KS = p2KL, p2KR, p2KJ, p2KS
        self.sfmv = sfmv
        self.sfxv = sfxv
        
    def start(self):
        running = True
        '''
        BUTTONS
        size nxn
        skill 6 buttons
        key binds 8 buttons

        range for sfmv & sfxV
        display
        '''
    
    def p1ChangeKey(self):
        pass

    def p2ChangeKey(self):
        pass
    
