''' So we have to create music application. It should allow users to download mp3 file of music and store it in local and play whenever they want in offline.
They should be able to create playlist. paste the url and get the song. Equalizer should be there. '''

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from kivy.lang import Builder
from pygame import mixer
import pafy
import os
import time

mixer.init()


filename = r"C:\Users\tkgowtham\Desktop_Folder\Python\alone2.wav"
mixer.music.load(filename)

class MusicApp(MDApp):
    def build(self):

        a = mixer.Sound(filename)
        total_length = a.get_length()
        mins, sec  = divmod(total_length, 60)
        total_length = float(round(mins)+(round(sec,1))/10)
        print(total_length)

        ini = mixer.music.get_pos()
        while ini < total_length:
            ini +=1
            time.sleep(1)
            
        
        label = MDLabel(text = "Welcome to Music App", halign = 'center',
                        pos_hint={'center_x':0.5,'center_y':0.95})

        music_title = MDLabel(text = os.path.basename(filename), halign = 'center', pos_hint={'center_x':0.5, 'center_y':0.75})
        
        icon_btn = MDIconButton(icon="play" ,pos_hint={'center_x':0.40,'center_y':0.5}  #On pressing this button it plays the music
                                ,on_release = self.playmusic)

        iconpause = MDIconButton(icon="pause",pos_hint={'center_x':0.50,'center_y':0.5},
                                 on_release = self.pausemusic)
        
        iconstop = MDIconButton(icon='stop', pos_hint={'center_x':0.60,'center_y':0.5},
                                 on_release = self.stopmusic)

        slider = MDSlider(min=0,max=total_length,value = ini
                          , pos_hint={'center_x':0.50,'center_y':0.6}, size_hint=(0.6,0.1))
        
        screen = Screen()
        screen.add_widget(label)
        screen.add_widget(music_title)
        screen.add_widget(icon_btn)
        screen.add_widget(iconstop)
        screen.add_widget(iconpause)
        screen.add_widget(slider)
        return screen

    global n, s
    n,s = 0,1              #n declares if the music is supposed to start or unpause
                            #s declares if the pause button is clicked at first without clicking the playmusic it just passes the function to the next statement.

    def playmusic(self,obj):
        if n == 0:
               #music is loaded and played.
            mixer.music.play()
            global s
            s = 2
        else:
            mixer.music.unpause()      
    
    def pausemusic(self,obj):
        if s == 1:
            pass
        else:
            global n
            n = 1
            mixer.music.pause()

    def stopmusic(self,obj):
        mixer.music.stop()    #Stoping the music
        global n, s
        n,s = 0,1               #Reseting the values.

MusicApp().run()
