from enum import Enum
import json

WIDTH = 150

def reaskForOption() -> int:
    return int(input('Please choose one of the options by typing its corresponding number.\n-> '))


class LineTypes(Enum):
    ACTION = 1
    SETTING = 2
    ACT = 3
    SCENE = 4
    DIALOGUE = 5
    DIRECTION = 6

class Character:
    def __init__(self, name_: str, description_: str) -> None:
        self.name = name_
        self.description = description_
    
    def convert(self):
        return {
            'name': self.name,
            'description': self.description,
        }
    
    def printDetails(self):
        print(self.name)
        print(self.description)


class Entity:
    def __init__(self, value_: str, type_: LineTypes, location_: int, character_: Character = None) -> None:
        self.type = type_
        self.location = location_
        self.character = character_
        self.value = value_
    
    def convert(self):

        if self.character:
            return {
                'type': self.type.value,
                'location': self.location,
                'character': self.character.convert(),
                'value': self.value,
            }
        else:
            return {
                'type': self.type.value,
                'location': self.location,
                'character': self.character,
                'value': self.value,
            }
    
    def printDetails(self):
        if self.character:
            print(self.character.name)
        print(self.value)


class Lines:
    def __init__(self, script_name_: str) -> None:
        self.curr_location = 0
        self.items = {
            'actions': [],
            'settings': [],
            'headers': [],
            'dialogues': [],
            'directions': [],
        }
        self.characters = []
        self.latest_info = {
            'Act': 0,
            'Scene': 0,
        }
        self.script_name = script_name_.lower().replace(' ', '_').replace('-', '_')
    
    def printCharacters(self):
        amt_chars = len(self.characters)
        if amt_chars == 0:
            print("You have no existing characters")
            return

        if amt_chars > 1:
            for c_index in range(amt_chars - 1):
                print(f'{self.characters[c_index].name} | ')
        print(f'{self.characters[amt_chars-1].name}')

    def addCharacter(self, name_: str) -> Character:
        desc = input(f'This is a new character!\nName: {name_}\nEnter description: ')
        return Character(name_=name_, description_=desc)

    def checkCharacter(self, name_: str, add: bool = False, view: bool = False) -> Character:
        curr_character = None
        char_name = name_.upper()

        for char in self.characters:
            if char.name == char_name:
                curr_character = char
                break
        
        if not curr_character and add:
            curr_character = self.addCharacter(name_=char_name)
            self.characters.append(curr_character)
        
        if curr_character and view:
            curr_character.printDetails()
        
        return curr_character
    
    def updateCharacter(self, c_name: str) -> bool:
        char = self.checkCharacter(name_=c_name, add=False, view=True)
        updateName = False
        updateDesc = False

        if char:
            old_name = char.name

            new_name = input(f'Enter a new name for {char.name}, or leave it blank and click enter if you do not want to change: ')
            if len(new_name.replace(' ', '')) > 0:
                answered = False
                while not answered:
                    done = int(input(f'1: Rewrite the name | 2: Update the name with {new_name}\n-> '))
                    while done != 1 and done != 2:
                        done = reaskForOption()

                    if done == 1:
                        answered = False
                    elif done == 2:
                        char.name = new_name
                        updateName = True
                        answered = True


            new_desc = input(f'Enter a new description for {char.name}, or leave it blank and click enter if you do not want to change: ')
            if len(new_name.replace(' ', '')) > 0:
                answered = False
                while not answered:
                    done = int(input(f'1: Rewrite the description | 2: Update the description with what was provided\n-> '))
                    while done != 1 and done != 2:
                        done = reaskForOption()

                    if done == 1:
                        answered = False
                    elif done == 2:
                        char.description = new_desc
                        updateDesc = True
                        answered = True
            
            for c in self.characters:
                if c.name == old_name:
                    if updateName:
                        c.name = char.name

                        for d in self.items['dialogues']:
                            if d.character.name == old_name:
                                d.character.name = char.name
                        for a in self.items['actions']:
                            if a.character.name == old_name:
                                a.character.name = char.name
                    if updateDesc:
                        c.description = char.description

                        for d in self.items['dialogues']:
                            if d.character.name == old_name:
                                d.character.description = char.description
                        for a in self.items['actions']:
                            if a.character.name == old_name:
                                a.character.description = char.description
                    return True
            
        else:
            return False

    

    def updateEntity(self, choice: str):
        end = False
        index = len(self.items[choice]) - 1

        if index < 0:
            print("There is nothing to update!")
            return

        while(index > -1 and not end):
            self.items[choice][index].printDetails()
            print()
            answer = int(input('1: Rewrite this line | 2: Next line | 3: End\n-> '))
            while answer != 1 and answer != 2 and answer != 3:
                answer = reaskForOption()
            
            if answer == 1:
                answered = False
                while not answered:
                    new_line = input("Rewrite the line: ")
                    done = int(input('1: Rewrite this line | 2: Update the line with the provided new line\n-> '))
                    while done != 1 and done != 2:
                        done = reaskForOption()

                    if done == 1:
                        answered = False
                    elif done == 2:
                        print("Updated!")
                        self.items[choice][index].value = new_line
                        answered = True
                            
                index -= 1
            elif answer == 2:
                index -= 1
            elif answer == 3:
                end = True
        


    def addItem(self, item: Entity, type_: str):
        self.curr_location += 1
        self.items[type_].append(item)

    
    def save(self):
        ## Save JSON
        stuff = {
            'end_location': self.curr_location,
            'items': {
                'actions': [ x.convert() for x in self.items['actions'] ],
                'settings': [ x.convert() for x in self.items['settings'] ],
                'headers': [ x.convert() for x in self.items['headers'] ],
                'dialogues': [ x.convert() for x in self.items['dialogues'] ],
                'directions': [ x.convert() for x in self.items['directions'] ],
            },
            'characters': [ x.convert() for x in self.characters ],
            'latest_info': self.latest_info,
            'script_name': self.script_name,
        }

        with open(f'raw_script_{self.script_name}.json', 'w+') as raw_lines:
            json.dump(stuff, raw_lines, indent = 4)


    
    def addAction(self, v: str, c_name: str):
        c = self.checkCharacter(name_=c_name, add=True)
        new_item = Entity(value_=v, type_=LineTypes.ACTION, location_=self.curr_location, character_=c)
        self.addItem(item=new_item, type_='actions')
    
    def addDialogue(self, v: str, c_name: str):
        c = self.checkCharacter(name_=c_name, add=True)
        new_item = Entity(value_=v, type_=LineTypes.DIALOGUE, location_=self.curr_location, character_=c)
        self.addItem(item=new_item, type_='dialogues')
    
    def addSetting(self, v: str):
        new_item = Entity(value_=v, type_=LineTypes.SETTING, location_=self.curr_location)
        self.addItem(new_item, type_='settings')
    
    def addDirection(self, v: str):
        new_item = Entity(value_=v, type_=LineTypes.DIRECTION, location_=self.curr_location)
        self.addItem(new_item, type_='directions')
    
    def addScene(self, v: str):
        self.latest_info['Scene'] = int(v)
        new_item = Entity(value_=str(self.latest_info['Scene']), type_=LineTypes.SCENE, location_=self.curr_location)
        self.addItem(item=new_item, type_='headers')
    
    def incrementAct(self):
        self.latest_info['Act'] += 1
        self.latest_info['Scene'] = 1
        new_item = Entity(value_=str(self.latest_info['Act']), type_=LineTypes.ACT, location_=self.curr_location)
        self.addItem(item=new_item, type_='headers')






def getSelection(script: Lines) -> bool:
    sel = int(input("1: Action | 2: Setting | 3: Header | 4: Dialogue | 5: Direction | 6: Update Script | 7: Update Character | 8: Done\n-> "))
    while sel < 1 or sel > 8:
        sel = reaskForOption()

    if sel == 8:
        return False

    if sel == 3:
        sel_2 = int(input("1: Increment Act | 2: Change Scene Number | 3: Nevermind\n-> "))
        while sel_2 < 1 or sel_2 > 2:
            sel_2 = reaskForOption()

        if sel_2 == 1:
            script.incrementAct()
            
        elif sel_2 == 2:
            new_num = input('Enter new Scene number: ')
            script.addScene(new_num)
        
        elif sel_2 == 3:
            return True

    
    elif sel == 1:
        script.printCharacters()
        character_name = ''
        value = ''

        answered_c = False
        while not answered_c:
            character_name = input('\nType the name of one of the characters above (or a new name for a new character) that this Action relates to: ')
            done = int(input('1: Rewrite this name | 2: You typed in the correct name | 3: Actually Nevermind\n-> '))

            while done < 1 and done > 3:
                done = reaskForOption()
            
            if done == 1:
                answered_c = False
            elif done == 2:
                answered_c = True
            elif done == 3:
                return True
        
        answered_v = False
        while not answered_v:
            value = input('Enter the action: ')
            done = int(input('1: Rewrite the action | 2: You typed in the correct action | 3: Actually Nevermind\n-> '))

            while done < 1 and done > 3:
                done = reaskForOption()
            
            if done == 1:
                answered_v = False
            elif done == 2:
                answered_v = True
            elif done == 3:
                return True
            
        script.addAction(v=value,c_name=character_name)

    
    elif sel == 4:
        script.printCharacters()
        character_name = ''
        value = ''

        answered_c = False
        while not answered_c:
            character_name = input('\nType the name of one of the characters above (or a new name for a new character) that this Dialogue belongs to: ')
            done = int(input('1: Rewrite this name | 2: You typed in the correct name | 3: Actually Nevermind\n-> '))

            while done < 1 and done > 3:
                done = reaskForOption()
            
            if done == 1:
                answered_c = False
            elif done == 2:
                answered_c = True
            elif done == 3:
                return True
        
        answered_v = False
        while not answered_v:
            value = input('Enter the dialogue: ')
            done = int(input('1: Rewrite the dialogue | 2: You typed in the correct dialogue | 3: Actually Nevermind\n-> '))

            while done < 1 and done > 3:
                done = reaskForOption()
            
            if done == 1:
                answered_v = False
            elif done == 2:
                answered_v = True
            elif done == 3:
                return True
            
        script.addDialogue(v=value,c_name=character_name)


    elif sel == 2:
        value = ''
        
        answered_v = False
        while not answered_v:
            value = input('Enter the setting: ')
            done = int(input('1: Rewrite the setting | 2: You typed in the correct setting | 3: Actually Nevermind\n-> '))

            while done < 1 and done > 3:
                done = reaskForOption()
            
            if done == 1:
                answered_v = False
            elif done == 2:
                answered_v = True
            elif done == 3:
                return True
        
        script.addSetting(v=value)
            

    elif sel == 5:
        value = ''
        
        answered_v = False
        while not answered_v:
            value = input('Enter the stage direction: ')
            done = int(input('1: Rewrite the stage direction | 2: You typed in the correct stage direction | 3: Actually Nevermind\n-> '))

            while done < 1 and done > 3:
                done = reaskForOption()
            
            if done == 1:
                answered_v = False
            elif done == 2:
                answered_v = True
            elif done == 3:
                return True
            
        script.addDirection(v=value)


    elif sel == 6:
        possible_choices = ['', 'actions', 'settings', 'dialogues', 'directions']
        
        answered = False
        while not answered:
            choice = int(input('1: Update Action | 2: Update Setting | 3: Update Dialogue | 4: Update Direction | 5: Nevermind\n-> '))

            while choice < 1 or choice > 5:
                choice = reaskForOption()
            
            if choice > 0 and choice < 5:
                script.updateEntity(choice=possible_choices[choice])
            elif choice == 5:
                return True


    elif sel == 7:
        script.printCharacters()
        
        answered = False
        while not answered:
            choice = input('Given the characters above, please type the name of the character you want to update: ')
            answered = script.updateCharacter(c_name=choice)

            while not answered:
                re_answer = int(input('That character does not exist!\n1: Try again with a different name | 2: Actually Nevermind\n-> '))
                while re_answer != 1 and re_answer != 2:
                    re_answer = reaskForOption()
                
                if re_answer == 1:
                    answered = script.updateCharacter(c_name=choice)
                elif re_answer == 2:
                    return True
            

    script.save()
    return True



def main():
    cont = True
    script_name = input('Enter script name: ')
    script = Lines(script_name_=script_name)

    while cont:
        cont = getSelection(script=script)

if __name__ == '__main__':
    main()