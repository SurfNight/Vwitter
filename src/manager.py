from typing import Tuple

class Manager():
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)
    
    def find_matching_command_and_text(self, text: str) -> Tuple:
        text_start = text[:10]
        for command in self.commands:
            for trigger in command.triggers:
                if trigger in text_start:
                    return (command, text.replace(trigger, '', 1))
        raise LookupError("No command found")
