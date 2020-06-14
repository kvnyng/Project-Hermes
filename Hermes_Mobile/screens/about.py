from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivy.uix.popup import Popup
from kivy.uix.label import Label

Builder.load_string("""
<AboutScreen>
    name: 'about'
    BoxLayout:
        orientation: 'vertical'
        Image:
            width: dp(200)
            source: '/home/benitez/Desktop/Project-Hermes/Screens_leo2/data/assets/static_img.jpg'
        Button:
            text:"Chamar ajuda"
            font_size: 45
            width: dp(20)
            on_release:
                print('calling the police')
                app.root.ids.scr_mngr.current = 'dashboard'
                root.manager.transition.direction = "left"

""")


class AboutScreen(Screen):
    pass
