from listener import Listener
from manager import Manager

def wait_for_valid_command():
    listener = Listener()
    manager = Manager()
    response = ""

    while True:
        response = listener.listen()
        if "Jarbas" in response:
            break

    manager.find_matching_command(response)
        
def get_twitter_creds():
    # TODO: Ask for Twitter API Credentials
    return
    

if __name__ == "__main__":
    get_twitter_creds()
    command = wait_for_valid_command()
