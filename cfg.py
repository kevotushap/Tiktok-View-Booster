from core import *

class cfg:
    def __init__(self) -> None:    
        self.config = json.loads(open('config.json', 'r').read())

    def get(self):
        video_url = self.config['video_url']
        return video_url