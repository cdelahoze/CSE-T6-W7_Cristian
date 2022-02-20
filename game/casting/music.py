
from pyray import *

class MusicBack:

    def __init__(self):

 
        self.init_VideoService()

        music = self.music_streem()

        self.load_music(music)

        while not window_should_close():
            self.update_music(music);
        self.unload_music(music)
        self.close_audio()
        self.close_window()
    
    
    def init_VideoService(self):

        init_window(900, 600, "Greed")


    def music_streem(self):
        init_audio_device()
        music = load_music_stream("Greed/audio/resources/country.mp3")
        return music
    
    def load_music(self, music):

        music.looping = True
        play_music_stream(music);

    def update_music(self, music):
        update_music_stream(music)
    
    def unload_music(self, music):
        unload_music_stream(music)

    def close_audio(self):
        close_audio_device()

    def close_window(self):
        close_window()