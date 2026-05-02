from enum import Enum
import json


def reaskForOption() -> int:
    return int(input('Please choose one of the options by typing its corresponding number.\n-> '))


def prompt_confirmed(prompt_text: str) -> str:
    """Prompt for a value and loop until the user confirms it."""
    while True:
        value = input(f'{prompt_text}\n-> ').strip()
        if not value:
            print('Value cannot be empty. Please try again.')
            continue
        done = int(input(f'1: Rewrite | 2: Confirm "{value}"\n-> '))
        while done != 1 and done != 2:
            done = reaskForOption()
        if done == 2:
            return value


def prompt_optional(prompt_text: str) -> str:
    """Prompt for an optional value. Returns empty string if skipped."""
    return input(f'{prompt_text} (leave blank to skip)\n-> ').strip()


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class LineType(Enum):
    SETTING         = 'setting'
    ACTION          = 'action'
    DIRECTION       = 'direction'
    DIALOGUE        = 'dialogue'
    DIALOGUE_ACTION = 'dialogue_action'


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

class Character:
    def __init__(self, name: str, description: str = '') -> None:
        self.name = name.upper()
        self.description = description

    def convert(self) -> dict:
        return {'name': self.name, 'description': self.description}

    def print_details(self):
        print(f'  {self.name}')
        if self.description:
            print(f'    {self.description}')


class Line:
    """A single line inside a Scene: setting, action, direction, or dialogue."""

    def __init__(self, type_: LineType, value: str,
                 character: 'Character' = None,
                 dialogue_action: str = '') -> None:
        self.type = type_
        self.value = value
        self.character = character
        self.dialogue_action = dialogue_action  # only meaningful when type == DIALOGUE

    def convert(self) -> dict:
        d = {
            'type': self.type.value,
            'value': self.value,
        }
        if self.character:
            d['character'] = self.character.convert()
        if self.dialogue_action:
            d['dialogue_action'] = self.dialogue_action
        return d

    def print_details(self):
        if self.character:
            print(f'      [{self.type.value.upper()}] {self.character.name}', end='')
            if self.dialogue_action:
                print(f' ({self.dialogue_action})', end='')
            print(f': {self.value}')
        else:
            print(f'      [{self.type.value.upper()}] {self.value}')


class Scene:
    def __init__(self, name: str, description: str = '') -> None:
        self.name = name
        self.description = description
        self.lines: list[Line] = []

    def add_line(self, line: Line):
        self.lines.append(line)

    def convert(self) -> dict:
        return {
            'name': self.name,
            'description': self.description,
            'lines': [l.convert() for l in self.lines],
        }

    def print_details(self):
        print(f'    Scene: {self.name}')
        if self.description:
            print(f'      ({self.description})')
        if not self.lines:
            print('      (no lines yet)')
        for line in self.lines:
            line.print_details()


class Act:
    def __init__(self, name: str, description: str = '') -> None:
        self.name = name
        self.description = description
        self.scenes: list[Scene] = []

    def add_scene(self, scene: Scene):
        self.scenes.append(scene)

    def current_scene(self) -> Scene:
        return self.scenes[-1] if self.scenes else None

    def convert(self) -> dict:
        return {
            'name': self.name,
            'description': self.description,
            'scenes': [s.convert() for s in self.scenes],
        }

    def print_details(self):
        print(f'  Act: {self.name}')
        if self.description:
            print(f'    ({self.description})')
        if not self.scenes:
            print('    (no scenes yet)')
        for scene in self.scenes:
            scene.print_details()


class Script:
    def __init__(self, title: str) -> None:
        self.title = title
        self.acts: list[Act] = []
        self.characters: list[Character] = []

    # ------------------------------------------------------------------
    # Character helpers
    # ------------------------------------------------------------------

    def print_characters(self):
        if not self.characters:
            print('No characters yet.')
            return
        print('Characters: ' + ' | '.join(c.name for c in self.characters))

    def find_character(self, name: str) -> Character:
        name = name.upper()
        for c in self.characters:
            if c.name == name:
                return c
        return None

    def get_or_create_character(self, name: str) -> Character:
        char = self.find_character(name)
        if not char:
            print(f'New character detected: {name.upper()}')
            desc = prompt_optional('Enter a description for this character')
            char = Character(name=name, description=desc)
            self.characters.append(char)
        return char

    def update_character(self, name: str) -> bool:
        char = self.find_character(name)
        if not char:
            return False

        print(f'\nEditing character: {char.name}')
        char.print_details()

        new_name = input(
            f'New name (leave blank to keep "{char.name}"): '
        ).strip()
        if new_name and new_name.upper() != char.name:
            old_name = char.name
            char.name = new_name.upper()
            for act in self.acts:
                for scene in act.scenes:
                    for line in scene.lines:
                        if line.character and line.character.name == old_name:
                            line.character.name = char.name

        new_desc = input(
            'New description (leave blank to keep current): '
        ).strip()
        if new_desc:
            char.description = new_desc
            for act in self.acts:
                for scene in act.scenes:
                    for line in scene.lines:
                        if line.character and line.character.name == char.name:
                            line.character.description = new_desc

        print(f'Character "{char.name}" updated.')
        return True

    # ------------------------------------------------------------------
    # Structure navigation
    # ------------------------------------------------------------------

    def current_act(self) -> Act:
        return self.acts[-1] if self.acts else None

    def current_scene(self) -> Scene:
        act = self.current_act()
        return act.current_scene() if act else None

    # ------------------------------------------------------------------
    # Adding structure
    # ------------------------------------------------------------------

    def add_act(self):
        name = prompt_confirmed('Enter Act name')
        desc = prompt_optional('Enter Act description')
        act = Act(name=name, description=desc)
        self.acts.append(act)
        print(f'\nAct "{name}" created. Now add the first scene.')
        self._add_scene_to_act(act)

    def add_scene(self):
        act = self.current_act()
        if not act:
            print('No act exists yet. Please create an Act first.')
            return
        self._add_scene_to_act(act)

    def _add_scene_to_act(self, act: Act):
        name = prompt_confirmed('Enter Scene name')
        desc = prompt_optional('Enter Scene description')
        scene = Scene(name=name, description=desc)
        act.add_scene(scene)
        print(f'Scene "{name}" added to Act "{act.name}".')

    # ------------------------------------------------------------------
    # Adding lines — all operate on the current scene
    # ------------------------------------------------------------------

    def _require_scene(self) -> Scene:
        scene = self.current_scene()
        if not scene:
            print('No scene exists yet. Please create an Act and Scene first.')
        return scene

    def add_setting(self):
        scene = self._require_scene()
        if not scene:
            return
        value = prompt_confirmed('Enter setting (e.g. INT. KITCHEN - DAY)')
        scene.add_line(Line(type_=LineType.SETTING, value=value))

    def add_direction(self):
        scene = self._require_scene()
        if not scene:
            return
        value = prompt_confirmed('Enter stage direction')
        scene.add_line(Line(type_=LineType.DIRECTION, value=value))

    def add_action(self):
        scene = self._require_scene()
        if not scene:
            return
        self.print_characters()
        char_name = prompt_confirmed('Enter character name for this action')
        char = self.get_or_create_character(char_name)
        value = prompt_confirmed('Enter the action')
        scene.add_line(Line(type_=LineType.ACTION, value=value, character=char))

    def add_dialogue(self):
        scene = self._require_scene()
        if not scene:
            return
        self.print_characters()
        char_name = prompt_confirmed('Enter character name for this dialogue')
        char = self.get_or_create_character(char_name)
        dlg_action = prompt_optional('Enter dialogue action (e.g. whispering)')
        value = prompt_confirmed('Enter the dialogue')
        scene.add_line(Line(
            type_=LineType.DIALOGUE,
            value=value,
            character=char,
            dialogue_action=dlg_action,
        ))

    # ------------------------------------------------------------------
    # Updating lines
    # ------------------------------------------------------------------

    def update_line_in_scene(self):
        scene = self._require_scene()
        if not scene:
            return
        if not scene.lines:
            print('No lines in the current scene yet.')
            return

        print(f'\nLines in scene "{scene.name}":')
        for i, line in enumerate(scene.lines):
            print(f'  {i + 1}.', end=' ')
            line.print_details()

        raw = input('Enter the number of the line to edit (or 0 to cancel): ').strip()
        if not raw.isdigit():
            return
        idx = int(raw) - 1
        if idx < 0 or idx >= len(scene.lines):
            return

        line = scene.lines[idx]
        new_value = prompt_confirmed(f'Rewrite the line (current: "{line.value}")')
        line.value = new_value
        print('Line updated.')

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------

    def print_structure(self):
        print(f'\n=== {self.title} ===')
        if not self.acts:
            print('  (no acts yet)')
        else:
            for act in self.acts:
                act.print_details()
        print()

    def print_current_context(self):
        act = self.current_act()
        scene = self.current_scene()
        act_label = f'Act: {act.name}' if act else 'No act'
        scene_label = f'Scene: {scene.name}' if scene else 'No scene'
        print(f'\n[{act_label}  |  {scene_label}]')

    # ------------------------------------------------------------------
    # Save
    # ------------------------------------------------------------------

    def save(self):
        data = {
            'title': self.title,
            'characters': [c.convert() for c in self.characters],
            'acts': [a.convert() for a in self.acts],
        }
        filename = (
            'raw_script_'
            + self.title.lower().replace(' ', '_').replace('-', '_')
            + '.json'
        )
        with open(filename, 'w+') as f:
            json.dump(data, f, indent=4)
        print(f'Saved → {filename}')


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

MAIN_MENU = (
    ' 1: Add Act       |  2: Add Scene     |  3: Add Setting\n'
    ' 4: Add Direction |  5: Add Action    |  6: Add Dialogue\n'
    ' 7: Update Line   |  8: Update Char   |  9: Show Script\n'
    '10: Done'
)


def run_menu(script: Script) -> bool:
    script.print_current_context()
    raw = input(f'\n{MAIN_MENU}\n-> ').strip()
    if not raw.isdigit():
        print('Please enter a number.')
        return True
    sel = int(raw)

    if sel == 10:
        return False
    elif sel == 1:
        script.add_act()
    elif sel == 2:
        script.add_scene()
    elif sel == 3:
        script.add_setting()
    elif sel == 4:
        script.add_direction()
    elif sel == 5:
        script.add_action()
    elif sel == 6:
        script.add_dialogue()
    elif sel == 7:
        script.update_line_in_scene()
    elif sel == 8:
        script.print_characters()
        name = input('Enter character name to edit: ').strip()
        if not script.update_character(name):
            print(f'Character "{name.upper()}" not found.')
    elif sel == 9:
        script.print_structure()
    else:
        print('Invalid option.')
        return True

    script.save()
    return True


def main():
    print('=== Script Maker ===')
    title = prompt_confirmed('Enter script title')
    script = Script(title=title)
    print(f'\nScript "{title}" created. Let\'s add the first Act.')
    script.add_act()

    while run_menu(script):
        pass

    print('\nScript complete. Goodbye!')


if __name__ == '__main__':
    main()
