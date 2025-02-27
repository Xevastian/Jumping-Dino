from game import Game
from button import Button, SettingsButton, SkillsButton
from util import load_save, updateInput
from utilSkill import load_save_skill, updateInputSkill
import pygame
x,y = 1280,720
screen = pygame.display.set_mode((x,y)) # Declaring window
clock = pygame.time.Clock()

pygame.display.set_caption("Dino Game") # Title
# gagawa ng menu loop

def get_Controls(save):
    return [x for i in save['controls'] for x in save['controls'][i].values()]

def checkDups(buttons):
    return [button.ctrl for button in buttons]

def get_buttons():
    save = load_save()
    actions = {'p1Left' : False,'p1Right': False,'p1Jump': False,'p1Skill': False,'p2Left': False,'p2Right': False,'p2Jump': False,'p2Skill': False}
    buttons = []
    ctrl = get_Controls(save)
    for i,j in enumerate(actions):
        x = 180 if i < 4 else 480
        y  = 220 + (i * 75) if i < 4 else 220 + ((i - 4) * 75)
        button = SettingsButton(x,y,50,j[2:],ctrl[i])
        buttons.append(button)

    return buttons

def get_SkillButtons():
    save = load_save_skill()
    actions = {'p1METEOR' : False,'p1BLIND': False,'p1SHIELD': False,'p2METEOR': False,'p2BLIND': False,'p2SHIELD': False}
    buttons = []
    active = save['skill']
    for i,j in enumerate(actions):
        x = 180 if i < 3 else 480
        y  = 520 + (i * 75) if i < 3 else 520 + ((i - 3) * 75)
        role = 'player1' if i < 3 else 'player2'
        button = SkillsButton(x,y,45,j[2:])
        if active[role] == j[2:].lower():
            button.isActivated = True
        buttons.append(button)

    return buttons

def settings():
    
    font = pygame.font.Font('FreeSansBold.ttf', 20) 
    p1Text, p2Text = font.render("Player 1", True, "Black"), font.render("Player 2", True, "Black")
    p1Rect,p2Rect = p1Text.get_rect(), p2Text.get_rect()
    p1Rect.center,p2Rect.center = (180,180),(480,180)
    skillsButton = get_SkillButtons()

    buttons = get_buttons()
    font = pygame.font.Font('FreeSansBold.ttf', 20) 
    running = True
    backButton = Button(170,70,240, 80, "Back")
    while running:
        mousepos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.isClicked(mousepos):
                    running = False
                for button in buttons:
                    if button.isClicked(mousepos):
                        for x in buttons:
                            x.isActivated = False
                        button.isActivated = True
                for i in range(len(skillsButton)):
                    if skillsButton[i].isClicked(mousepos):
                       role = 'player1' if i < 3 else 'player2'
                       updateInputSkill(role,skillsButton[i].text)
                       skillsButton = get_SkillButtons()
            if event.type == pygame.KEYDOWN:
                value = event.key
                for x in range(len(buttons)):
                    if buttons[x].isActivated and not value in checkDups(buttons):
                        role = 'player1' if x < 4 else 'player2'
                        key = buttons[x].text
                        updateInput(role,key,value)
                        buttons = get_buttons()
                        
                
        screen.fill("White")
        backButton.draw(screen)
        for button in buttons: 
            button.draw(screen)
        for button in skillsButton:
            button.draw(screen)
        screen.blit(p1Text,p1Rect)
        screen.blit(p2Text,p2Rect)
        pygame.display.update()
        clock.tick(60)
    return
def main():
    
    StartButton = Button(x//2, (y//2) - 120, 240, 80, "Start")
    SettingsButton = Button(x//2,(y//2) ,240,80, "Settings")
    ExitButton = Button(x//2,(y//2) + 120,240,80, "Exit")
    '''
    count down
    cooldown display

    button2 for settings
    settings display and input key manipulation
    key bindings, skill picking, sfx, sfm, back button

    button for single player(optional)

    button for exit
    '''
    running = True
    while running:
        mousepos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if StartButton.isClicked(mousepos):
                    game = Game(screen,"meteor","blind")
                    game.start()
                elif ExitButton.isClicked(mousepos):
                    running = False
                elif SettingsButton.isClicked(mousepos):
                    settings()
        
        screen.fill("Green")
        StartButton.draw(screen)   
        SettingsButton.draw(screen)
        ExitButton.draw(screen) 
        pygame.display.update()
        clock.tick(60)
    
main()
#buttons
#pag clinick ung 2p game magrrun game.start(screen)
