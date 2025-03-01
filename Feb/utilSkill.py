import os, json, pygame

def load_existing_save(savefile):
    with open(os.path.join(savefile), 'r+') as file:
        controls = json.load(file)
    return controls

def write_save(data):
    with open(os.path.join(os.getcwd(),'saveSkill.json'), 'w') as file:
        json.dump(data, file)

def load_save_skill():
    try:
    # Save is loaded 
        save = load_existing_save('saveSkill.json')
    except:
    # No save file, so create one
        save = create_save()
        write_save(save)
    return save


def create_save():
    new_save = {
    "skill":{
        "player1" :"meteor",
        "player2" :"meteor"
        }
    }

    return new_save

def updateInputSkill(role,value):
    data = load_save_skill()
    data['skill'][role] = value.lower()
    with open('saveSkill.json','w') as f:
        f.write(json.dumps(data))