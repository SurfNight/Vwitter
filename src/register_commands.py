from manager import Manager

manager = Manager()

def register_command(klass) -> None:
    """
    This decorator registers a class on `manager` global object
    """
    manager.add(klass)

def get_current_manager():
    """
    This function returns the current manager
    """
    return manager
