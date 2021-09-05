from typing import Tuple, Dict

class Manager():
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)
    
    def find_matching_command_and_text(self, text: str) -> Tuple:
        print("validando texto")
        text_start = text[:10]
        breakpoint()
        for command in self.commands:
            print(command)
            for trigger in command.triggers:
                print(trigger)
                if trigger in text_start:
                    print(f"e o trigger: {trigger}")
                    return (command, text.replace(trigger, '', 1))
        raise LookupError("No command found")
