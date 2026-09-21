from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from kivy.clock import Clock
text = get_display(reshape("ترانيم"))
text1 = get_display(reshape("احكي يا تاريخ"))
text2 = get_display(reshape("►مارمينا"))
text3 = get_display(reshape("||مارمينا"))
sound1 = SoundLoader.load("music.1.ogg")
Window.size = (320, 500)
Window.clearcolor = (185/255, 122/255, 86/255, 1)

Builder.load_string('''
<MainScreen>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
    BoxLayout:
        orientation: 'vertical'
        Button:
            size_hint: None, None
            background_normal: 'icon.png'
            on_press:root.manager.current = 'sm2'
            font_name: "NotoSansArabic-VariableFont_wdth,wght.ttf"            
            text:app.text
            halign: "right"
            color:(0,0,0,1)          
<SettingScreen>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
    GridLayout: 
        cols:4
        rows:5
        Button:
            text:app.text1
            font_name: "NotoSansArabic-VariableFont_wdth,wght.ttf"
            on_press:root.manager.current = 'sm3'
            color:(0,0,0,1)
        Button:
            text:"sm4"
            on_press:root.manager.current = 'sm4'
        Button:
            text:"sm5"
            on_press:root.manager.current = 'sm5'
        Button:
            text:"sm6"
            on_press:root.manager.current = 'sm6'
        Button:
            text:"sm7"
            on_press:root.manager.current = 'sm7'
        Button:
            text:"sm8"
            on_press:root.manager.current = 'sm8'
        Button:
            text:"sm9"
            on_press:root.manager.current = 'sm9'
        Button:
            text:"sm10"
            on_press:root.manager.current = 'sm10'
        Button:
            text:"sm11"
            on_press:root.manager.current = 'sm11'
        Button:
            text:"sm12"
            on_press:root.manager.current = 'sm12'
        Button:
            text:"sm13"
            on_press:root.manager.current = 'sm13' 
        Button:
            text:"sm14"
            on_press:root.manager.current = 'sm14'
        Button:
            text:"sm15"
            on_press:root.manager.current = 'sm15'
        Button:
            text:"sm16"
            on_press:root.manager.current = 'sm16'
        Button:
            text:"sm17"
            on_press:root.manager.current = 'sm17' 
        Button:
            text:"sm18"
            on_press:root.manager.current = 'sm18' 
        Button:
            text:"sm19"
            on_press:root.manager.current = 'sm19' 
        Button:
            text:"sm20"
            on_press:root.manager.current = 'sm20' 
        Button:
            text:"sm21"
            on_press:root.manager.current = 'sm21' 
        Button:
            text:"sm22"
            on_press:root.manager.current = 'sm22' 
                       
<Screen1>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
    GridLayout:
        cols:2
        rows:1
        Button:
            text:app.text2
            font_name: "C:/Windows/Fonts/segoeui.ttf"
            on_press:app.play_song(self) 
            size_hint: (None, None)
      
        Button:
            text: app.text3
            font_name: "NotoSansArabic-VariableFont_wdth,wght.ttf"
            on_press:app.stop_song(self)
            size_hint: (None, None)  
<Screen2>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False

<Screen3>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False

<Screen4>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen5>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen6>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen7>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen8>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen9>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen10>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen11>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen12>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen13>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False

<Screen14>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen15>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen16>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen17>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen18>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen19>:    
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False
<Screen20>:
    FloatLayout:
        Image:
            source: 'background.png'
            allow_stretch: True
            keep_ratio: False

                     
''')


class MainScreen(Screen):
    pass


class SettingScreen(Screen):
    pass

class Screen1(Screen):
    pass   

class Screen2(Screen):
    pass
class Screen3(Screen):
    pass
class Screen4(Screen):
    pass
class Screen5(Screen):
    pass
class Screen6(Screen):
    pass
class Screen7(Screen):
    pass
class Screen8(Screen):
    pass
class Screen9(Screen):
    pass
class Screen10(Screen):
    pass
class Screen11(Screen):
    pass
class Screen12(Screen):
    pass
class Screen13(Screen):
    pass
class Screen14(Screen):
    pass
class Screen15(Screen):
    pass
class Screen16(Screen):
    pass
class Screen17(Screen):
    pass
class Screen18(Screen):
    pass
class Screen19(Screen):
    pass
class Screen20(Screen):
    pass
class MyApp(App):


    text = text
    text1 = text1
    text2 = text2
    text3 = text3
    def build(self):
        layout = FloatLayout()

        # 2. إضافة صورة الخلفية (تتمدد تلقائياً لتغطي الشاشة)
        bg = Image(
            source='background.png', # اسم ملف الصورة
            allow_stretch=True,      # السماح بالتمدد
            keep_ratio=False          # ملء الشاشة بالكامل دون ترك حواف
        )
        layout.add_widget(bg)
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='sm1'))
        sm.add_widget(SettingScreen(name='sm2'))
        sm.add_widget(Screen1(name='sm3'))
        sm.add_widget(Screen2(name='sm4'))
        sm.add_widget(Screen3(name='sm5'))
        sm.add_widget(Screen4(name='sm6'))
        sm.add_widget(Screen5(name='sm7'))
        sm.add_widget(Screen6(name='sm8'))
        sm.add_widget(Screen7(name='sm9'))
        sm.add_widget(Screen8(name='sm10'))
        sm.add_widget(Screen9(name='sm11'))
        sm.add_widget(Screen10(name='sm12'))
        sm.add_widget(Screen11(name='sm13'))
        sm.add_widget(Screen12(name='sm14'))
        sm.add_widget(Screen13(name='sm15'))
        sm.add_widget(Screen14(name='sm16'))
        sm.add_widget(Screen15(name='sm17'))
        sm.add_widget(Screen16(name='sm18'))
        sm.add_widget(Screen17(name='sm19'))
        sm.add_widget(Screen18(name='sm20'))
        sm.add_widget(Screen19(name='sm21'))
        sm.add_widget(Screen20(name='sm22'))
                

        
        return sm
    def stop_song(self, *args):
        global sound1
        if sound1 :
            # حفظ الموضع بالثواني قبل الإيقاف
            self.sound_position = sound1.get_pos()
            sound1.stop()
    def play_song(self, *args):
        global sound1
        if sound1:
                sound1.play()
        if hasattr(self, 'sound_position'):
                sound1.seek(self.sound_position)
if __name__ == '__main__':
    MyApp().run()