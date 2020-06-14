from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivy.uix.popup import Popup
from kivy.uix.label import Label

Builder.load_string("""
<AboutScreen>
    name: 'about'
    GridLayout:
        cols:1
        GridLayout:
            cols: 2
            Image:
                source: '/home/benitez/Desktop/Project-Hermes/Screens_leo2/data/assets/graph1.jpg'
            Image:
                source: '/home/benitez/Desktop/Project-Hermes/Screens_leo2/data/assets/graph2.jpg'
        GridLayout:
            # I did a second gridLayout only to change the proportios on screen... there must be a better way
            cols: 2
            Image:
                source: '/home/benitez/Desktop/Project-Hermes/Screens_leo2/data/assets/graph3.jpg'
            Image:
                source: '/home/benitez/Desktop/Project-Hermes/Screens_leo2/data/assets/graph4.jpg'


        Button:
            text:"Call the police"
            on_release:
                print('fuck the police')
                app.root.ids.scr_mngr.current = 'dashboard'
                root.manager.transition.direction = "left"

""")


class AboutScreen(Screen):
    def popup(self):
        print('open pop!')
        show = MyPopup()
        popupWindow = Popup(title="More information", content=Label(text='Hello world'),
                            size_hint=(None, None), size=(400, 400))
        popupWindow.open()


class MyPopup(Screen):
    pass
