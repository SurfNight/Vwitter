class Command():
    def __init__(self, name, description, triggers):
        self.name = name
        self.description = description
        self.triggers = [triggers]
        
    def run(self):
        raise NotImplementedError("Should have implemented run method")