import os, json, pygame

def load_existing_save(savefile):
    with open(os.path.join(savefile), 'r+') as file:
        controls = json.load(file)
    return controls

def write_save(data):
    with open(os.path.join(os.getcwd(),'Feb/save.json'), 'w') as file:
        json.dump(data, file)

def load_save():
    try:
    # Save is loaded 
        save = load_existing_save('Feb/save.json')
    except:
    # No save file, so create one
        save = create_save()
        write_save(save)
    return save


def create_save():
    new_save = {
    "controls":{
        "player1" :{"Left": pygame.K_a, "Right": pygame.K_d, "Jump": pygame.K_w, "Skill": pygame.K_e},
        "player2" :{"Left": pygame.K_LEFT, "Right": pygame.K_RIGHT, "Jump": pygame.K_UP, "Skill": pygame.K_LSHIFT}
        }
    }

    return new_save

def updateInput(role,key,value):
    data = load_save()
    data['controls'][role][key] = value
    with open('Feb/save.json','w') as f:
        f.write(json.dumps(data))