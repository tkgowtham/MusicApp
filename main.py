''' So we have to create music application. It should allow users to download mp3 file of music and store it in local and play whenever they want in offline.
They should be able to create playlist. paste the url and get the song. Equalizer should be there. '''

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDIconButton
#from kivy.lang import Builder
from pygame import mixer
import pafy

mixer.init()


class MusicApp(MDApp):
    def build(self):
        #screen_build = Builder.load_string(navigation_helper)
        
        label = MDLabel(text = "Welcome to Music App", halign = 'center',
                        pos_hint={'center_x':0.5,'center_y':0.95})
        
        icon_btn = MDIconButton(icon="play" ,pos_hint={'center_x':0.45,'center_y':0.5}  #On pressing this button it plays the music
                                ,on_release = self.playmusic)
        
        iconpause = MDIconButton(icon='stop', pos_hint={'center_x':0.55,'center_y':0.5},
                                 on_release = self.stopmusic)
        
        screen = Screen()
        screen.add_widget(label)
        screen.add_widget(icon_btn)
        screen.add_widget(iconpause)
        return screen

    def playmusic(self,obj):
        mixer.music.load(r"C:\Users\gowthamkamalasekar\Desktop\alone.mp3")   #music is loaded and played.
        mixer.music.play()

    def stopmusic(self,obj):
        mixer.music.stop()                       #Stoping the music
            

MusicApp().run()
