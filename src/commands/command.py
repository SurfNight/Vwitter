class Command():
    name = None
    description = None
    triggers = None

    def run(self):
        raise NotImplementedError("Should have implemented run method")