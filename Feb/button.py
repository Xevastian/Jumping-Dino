import pygame

class Button:
    def __init__(self,x,y,l,h,text):
        self.x = x 
        self.y = y 
        
        self.button = pygame.Rect(self.x - (l // 2), self.y - (h // 2), l,h)
        self.text = text

    def draw(self,screen):
        font = pygame.font.Font('FreeSansBold.ttf', 32) 
        ButtonText = font.render(self.text,True,"Black")
        textRect = ButtonText.get_rect()
        textRect.center = (self.x,self.y)
        pygame.draw.rect(screen,"Red", self.button)
        screen.blit(ButtonText,textRect)

    
    def isClicked(self,mouseLoc):
        return self.button.collidepoint(mouseLoc)        

class SettingsButton(Button):
    def __init__(self,x,y,size,text,ctrl):
        super().__init__(x,y,size * 3,size,text)
        self.isActivated = False
        self.ctrl = ctrl
        self.size = size
    
    def draw(self,screen):
        font = pygame.font.Font('FreeSansBold.ttf', 20) 
        color = "Blue" if self.isActivated else "Red"
        ButtonText = font.render(pygame.key.name(self.ctrl),True,"Black")
        desc = font.render(self.text,True,"Black")
        textRect, descRect = ButtonText.get_rect(), desc.get_rect()
        textRect.center, descRect.center = (self.x,self.y), (self.x - self.size * 2.5 , self.y) 
        pygame.draw.rect(screen,color, self.button)
        screen.blit(ButtonText,textRect)
        screen.blit(desc, descRect)

class SkillsButton(Button):
    def __init__(self,x,y,size,text):
        super().__init__(x,y,size * 3,size,text)
        self.isActivated = False
        self.size = size
    
    def draw(self,screen):
        font = pygame.font.Font('FreeSansBold.ttf', 20) 
        color = "Blue" if self.isActivated else "Red"
        ButtonText = font.render(self.text,True,"Black")
        textRect = ButtonText.get_rect()
        textRect.center = (self.x,self.y)
        pygame.draw.rect(screen,color, self.button)
        screen.blit(ButtonText,textRect)