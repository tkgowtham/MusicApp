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
        
        icon_btn = MDIconButton(icon="play" ,pos_hint={'center_x':0.40,'center_y':0.5}  #On pressing this button it plays the music
                                ,on_release = self.playmusic)

        iconpause = MDIconButton(icon="pause",pos_hint={'center_x':0.50,'center_y':0.5},
                                 on_release = self.pausemusic)
        
        iconstop = MDIconButton(icon='stop', pos_hint={'center_x':0.60,'center_y':0.5},
                                 on_release = self.stopmusic)
        
        screen = Screen()
        screen.add_widget(label)
        screen.add_widget(icon_btn)
        screen.add_widget(iconstop)
        screen.add_widget(iconpause)
        return screen

    global n
    n = 1

    def playmusic(self,obj):
        if n == 1:
            mixer.music.load(r"C:\Users\gowthamkamalasekar\Desktop\alone.mp3")   #music is loaded and played.
            mixer.music.play()
        else:
            mixer.music.unpause()      
    
    def pausemusic(self,obj):
        global n
        n = 0
        mixer.music.pause()

    def stopmusic(self,obj):
        mixer.music.stop()    #Stoping the music
        global n
        n = 1

MusicApp().run()
