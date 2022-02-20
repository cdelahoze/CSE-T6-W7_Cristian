from pyray import *

from game.casting.actor import Actor
class VideoService(Actor):

    def __init__(self):
        
        self.init_VideoService()
        
        while not window_should_close():
            self.actor_value()
        self.close_window()
    

    def init_VideoService(self):
        init_window(900, 600, "Greed")

    
    def close_window(self):
        close_window()