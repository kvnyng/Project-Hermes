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
            MDLabel:
                text: 'fuck Trump1'#ut.get_data('texts')['about']
                
            MDLabel:
                text: 'fuck Trump2'#ut.get_data('texts')['about']
        GridLayout:
            # I did a second gridLayout only to change the proportios on screen... there must be a better way
            cols: 2
            Label:
                text: 'fuck Trump3'#ut.get_data('texts')['about']
                on_touch_down: root.popup()
            Label:
                text: 'fuck Trump3'#ut.get_data('texts')['about']
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
